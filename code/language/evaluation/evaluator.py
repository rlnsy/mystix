from __future__ import annotations
from typing import TYPE_CHECKING as STATIC_CHECK
if STATIC_CHECK:
    from code.language.shared.ast import *
from code.language.shared.ast.visitor import Visitor
from code.language.shared.primitives import values, numerical
from code.targets.analysis.math import apply_fn, apply_op, apply_qk
from .errors import LanguageError
from .vars import Environment
from code.targets.visualization.graphs import GraphManager
from threading import Thread


class Evaluator(Visitor):

    def __init__(self, graphics: bool = False):
        self.env = Environment()
        self.graphics_enabled: bool = graphics
        self.gm = GraphManager()

    def evaluate(self, p: Program) -> int:
        logic = Thread(target=lambda: self.visit_program(p))
        logic.start()
        if self.graphics_enabled:
            self.gm.graphics.display(ttl=3000)  # every program lasts 3 seconds TODO
        logic.join()    # TODO: find a way to get the return value
        self.gm.clean()
        return 0

    def visit_program(self, p: Program):
        pass

    def visit_body(self, b: Body):
        pass
    
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
        pass

    def visit_reporting(self, r: Reporting):
        pass

    def visit_var(self, v: Var):
        pass

    def visit_source(self, s: Source):
        pass

    def visit_type(self, t: Type):
        pass

    def visit_value(self, v: Value):
        pass

    def visit_graph(self, g: Graph):
        pass

    def visit_var_axis(self, va: VarAxis):
        pass

    def visit_func_axis(self, fa: FuncAxis):
        pass

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