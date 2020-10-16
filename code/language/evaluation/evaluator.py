from __future__ import annotations
from typing import TYPE_CHECKING as STATIC_CHECK, List, Callable
if STATIC_CHECK:
    from code.language.shared.ast import *
from code.language.shared.ast.visitor import Visitor
from code.language.shared.primitives import values, numerical
from code.language.shared.primitives.graphs import (
    Graph as ConcreteGraphType, LineXYGraph)
from code.targets.visualization.graphs import GraphManager
from concurrent.futures import ThreadPoolExecutor
import time
from code.targets.data import DataLoader
from code.language.shared.primitives.types import Types
from code.targets.analysis.math import apply_fn, apply_op, apply_qk
from .errors import LanguageError
from .vars import Environment
from collections import defaultdict


TYPES = {
    Types.NUMBER: values.NumericalValue,
    Types.BINARY: values.BinaryValue,
    Types.CATEGORY: values.CategoricalValue
}


class Evaluator(Visitor):

    def __init__(self, graphics: bool = False):
        """
        :param graphics: Controls graphics functionality
        if set to False, any behaviour involving graphics
        will simply not occur.
        """
        self.env = Environment()
        self.gm = GraphManager() if graphics else None
        self.plots: List = []
        self.data = DataLoader()
        # maps a source name to a field mapping dict
        self.maps: defaultdict = defaultdict(lambda: {})
        # for source name provide a list of procedures to execute
        self.events: defaultdict = defaultdict(lambda: [])
        self.sources: List[str] = []

    def do_graphics(self, p: Callable):
        if self.gm is not None:
            p(self.gm)

    def update_plots(self):
        # vars -> plots
        for pl in self.plots:
            g: str = pl[0]
            a1: Axis = pl[1]
            a2: Axis = pl[2]
            x = a1.accept(self)
            y = a2.accept(self)

            def add(m: GraphManager):
                m.add_plot_data(g, [x.value], [y.value])
            self.do_graphics(add)

    def update_sources(self):
        # loader -> vars
        for s in self.sources:
            data: List[dict] = self.data.get_new(s)
            maps = self.maps[s]
            for d in data:
                rs = [e() for e in self.events[s]]
                for f in maps:
                    if f in d:
                        val = self.env.get_val(maps[f])
                        d_val = d[f]
                        if isinstance(val, values.NumericalValue):
                            if type(d_val) is int:
                                val = values.IntegerValue(d_val)
                            elif type(d_val) is float:
                                val = values.FloatValue(d_val)
                            else:
                                raise LanguageError(
                                    "Cannot map %s to number %s"
                                    % (str(d_val), maps[f]))
                        elif isinstance(val, values.BinaryValue):
                            if type(d_val) is bool:
                                val = values.BinaryValue(d_val)
                            else:
                                raise LanguageError(
                                    "Cannot map %s to binary %s"
                                    % (str(d_val), maps[f]))
                        else:  # CategoricalValue
                            if type(d_val) is not dict and type(d_val) is not list:
                                val = values.CategoricalValue(str(d_val))
                            else:
                                raise LanguageError("Cannot map %s to %s"
                                                    % (str(d_val), maps[f]))
                        self.env.set_val(maps[f], val)
                        self.update_plots()
                    else:
                        raise LanguageError("Source %s does not have a field %s"
                                            % (s, f))

    def execute(self, p: Program, duration: int):
        # internal clock
        for i in range(int(duration/1000)):
            self.update_sources()
            time.sleep(1)
        return 0, None

    def evaluate(self, p: Program):

        # perform the initial traversal
        try:
            self.visit_program(p)
        except LanguageError as e:
            print("\nERROR: %s\n" % str(e))
            return 1, e

        duration = 5000  # every program lasts 10 seconds TODO
        exit_val = 0

        def runtime():
            try:
                return self.execute(p, duration)
            except LanguageError as e:
                print("Detected a language error")

                def close(m: GraphManager):
                    m.close()
                self.do_graphics(close)

                return 1, e
        with ThreadPoolExecutor() as threads:
            logic = threads.submit(runtime)

            def start(m: GraphManager):
                m.graphics.display(ttl=duration)
            self.do_graphics(start)

            exit_val, err = logic.result()
            print("Program execution completed!")
            if exit_val != 0:
                print("\nERROR: %s\n" % str(err))

            def clean(m: GraphManager):
                m.clean()
            self.do_graphics(clean)

        return exit_val, err

    def visit_program(self, p: Program):
        p.body.accept(self)

    def visit_body(self, b: Body):
        for c in b.commands:
            c.accept(self)
    
    def visit_loader(self, l: Loader):
        # TODO: add source as a value in environment?
        v: Var = l.name
        self.data.register_source(l.source.accept(self), v.name)
        self.sources.append(v.name)

    def visit_mapper(self, m: Mapper):
        v_name = m.decl.accept(self)
        # TODO: source should be stored in environment
        s_name = m.src.name
        self.maps[s_name][m.tbl_field] = v_name

    def visit_declare(self, d: Declare) -> str:
        t: Types = d.type.accept(self)
        # Enumerate the type cases
        c = TYPES[t]
        self.env.extend(d.var.name, c())
        return d.var.name

    def visit_assigner(self, a: Assigner) -> values.Value:
        n: str = a.decl.accept(self)
        return self.env.set_val(n, a.value.value)

    def visit_trigger(self, t: Trigger):
        # TODO: source should be stored in environment
        self.events[t.var1.name].append(lambda: t.math_funcs.accept(self))

    def visit_plotter(self, pltr: Plotter):
        graph: ConcreteGraphType = pltr.graph.accept(self)
        line: bool = isinstance(graph, LineXYGraph)

        def add_data(m: GraphManager):
            m.add_plot(pltr.graph_name, line_plot=line)
        self.do_graphics(add_data)

        self.plots.append((pltr.graph_name, pltr.x, pltr.y))

    def visit_reporting(self, r: Reporting):
        pass

    def visit_var(self, v: Var) -> values.Value:
        return self.env.get_val(v.name)

    def visit_source(self, s: Source) -> str:
        return s.url

    def visit_type(self, t: Type):
        return t.type

    def visit_value(self, v: Value) -> values.Value:
        return v.value

    def visit_graph(self, g: Graph) -> ConcreteGraphType:
        return g.graph

    def visit_var_axis(self, va: VarAxis) -> values.Value:
        return va.var.accept(self)

    def visit_func_axis(self, fa: FuncAxis):
        return fa.fun.accept(self)

    def visit_math_funcs(self, mf: MathFuncs):
        for func in mf.mth_func_lst:
            func.accept(self)
            pass
        pass

    def visit_simple_func(self, smp: SimpleFunc) -> values.Value:
        if isinstance(smp.rhs.value, values.NumericalValue):
            v: values.Value = self.env.get_val(smp.impacted_var.name)
            if isinstance(v, values.NumericalValue):
                operand = smp.op.accept(self)
                return apply_op(operand,v, smp.rhs.value)
            else:
                raise LanguageError("Simple Functions only accept numbers.")
        else:
            raise LanguageError("Simple Functions only accept numbers.")

    def visit_increment(self, i: Increment) -> values.Value:
        v: values.Value = self.env.get_val(i.impacted_var.name)
        if isinstance(v, values.NumericalValue):
            return apply_qk("inc",v)
        else:
            raise LanguageError("Fast Functions only accept numbers.")

    def visit_decrement(self, d: Decrement) -> values.Value:
        v: values.Value = self.env.get_val(d.impacted_var.name)
        if isinstance(v, values.NumericalValue):
            return apply_qk("dec",v)
        else:
            raise LanguageError("Fast Functions only accept numbers.")

    def visit_builtin_func(self, bltn: BuiltinFunc):
        v: values.Value = self.env.get_val(bltn.input.name)
        if isinstance(v, values.NumericalValue):
            return apply_fn(bltn.fun, v)
        else:
            raise LanguageError("BuiltIn Functions only accept numbers.")

    def visit_operand(self, op: Operand) -> numerical.NumOp:
        return op.op
