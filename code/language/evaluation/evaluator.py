from __future__ import annotations
from typing import TYPE_CHECKING as STATIC_CHECK
if STATIC_CHECK:
    from code.language.shared.ast import *
from .visitor import Visitor

class Evaluator(Visitor):

    def evaluate(self, p: Program) -> int:
        return 0  # stub

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
        pass

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
        pass

    def visit_simple_func(self, smp: SimpleFunc):
        pass

    def visit_increment(self, i: Increment):
        pass

    def visit_decrement(self, d: Decrement):
        pass

    def visit_builtin_func(self, bltn: BuiltinFunc):
        pass

    def visit_operand(self, op: Operand):
        pass