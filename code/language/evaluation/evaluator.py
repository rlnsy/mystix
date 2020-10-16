from __future__ import annotations
from typing import TYPE_CHECKING as STATIC_CHECK, List
if STATIC_CHECK:
    from code.language.shared.ast import *
from code.language.shared.ast.visitor import Visitor
from code.language.shared.primitives import values, numerical
from code.language.shared.primitives.graphs import Graph as ConcreteGraphType, \
    LineXYGraph, ScatterXYGraph
from code.targets.analysis.math import apply_fn, apply_op, apply_qk
from .errors import LanguageError
from .vars import Environment
from code.targets.visualization.graphs import GraphManager
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor
import time


class Evaluator(Visitor):

    def __init__(self, graphics: bool = False):
        """
        :param graphics: Controls graphics functionality
        if set to False, any behaviour involving graphics
        will simply not occur.
        """
        self.env = Environment()
        self.graphics_enabled: bool = graphics
        self.gm = GraphManager()
        self.plots: List = []

    def execute(self, p: Program, duration: int):
        # internal clock
        for i in range(int(duration/1000)):
            for pl in self.plots:
                g: str = pl[0]
                a1: Axis = pl[1]
                a2: Axis = pl[2]
                x = a1.accept(self)
                y = a2.accept(self)
                self.gm.add_plot_data(g, [0.0], [0.0])
            time.sleep(1)
        return 0, None

    def evaluate(self, p: Program):

        # perform the initial traversal
        self.visit_program(p)

        duration = 5000  # every program lasts 10 seconds TODO
        exit_val = 0

        def runtime():
            try:
                return self.execute(p, duration)
            except LanguageError as e:
                print("Detected a language error")
                self.gm.close()
                return 1, e
        with ThreadPoolExecutor() as threads:
            logic = threads.submit(runtime)
        # logic = Thread(target=runtime)
        # logic.start()
            if self.graphics_enabled:
                # TODO: running without graphics currently breaks tests
                print("Running graphics features")
                self.gm.graphics.display(ttl=duration)
        # logic.join()
            exit_val, err = logic.result()
            print("Program execution completed!")
            if exit_val != 0:
                print("\nERROR: %s\n" % str(err))
            self.gm.clean()
        return exit_val, err

    def visit_program(self, p: Program):
        p.body.accept(self)

    def visit_body(self, b: Body):
        for c in b.commands:
            c.accept(self)
    
    def visit_loader(self, l: Loader):
        pass

    def visit_mapper(self, m: Mapper):
        pass

    def visit_declare(self, d: Declare):
        pass

    def visit_assigner(self, a: Assigner):
        pass

    def visit_trigger(self, t: Trigger):
        t.math_funcs.accept(self)

    def visit_plotter(self, pltr: Plotter):
        graph: ConcreteGraphType = pltr.graph.accept(self)
        line: bool = isinstance(graph, LineXYGraph)
        self.gm.add_plot(pltr.graph_name, line_plot=line)
        self.plots.append((pltr.graph_name, pltr.x, pltr.y))

    def visit_reporting(self, r: Reporting):
        pass

    def visit_var(self, v: Var) -> values.Value:
        return self.env.get_val(v.name)

    def visit_source(self, s: Source):
        pass

    def visit_type(self, t: Type):
        pass

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