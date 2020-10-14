from code.language.shared.ast import Program
from .visitor import Visitor

class Evaluator(Visitor):

    def evaluate(self, p: Program) -> int:
        return 0  # stub

    def visit_program(self, p):
        pass

    def visit_body(self, b):
        pass
    
    def visit_loader(self, l):
        pass

    def visit_mapper(self, m):
        pass

    def visit_declare(self, d):
        pass

    def visit_assigner(self, a):
        pass

    def visit_trigger(self, t):
        pass

    def visit_plotter(self, pltr):
        pass

    def visit_reporting(self, r):
        pass

    def visit_var(self, v):
        pass

    def visit_source(self, s):
        pass

    def visit_type(self, t):
        pass

    def visit_value(self, v):
        pass

    def visit_graph(self, g):
        pass

    def visit_var_axis(self, va):
        pass

    def visit_func_axis(self, fa):
        pass

    def visit_math_funcs(self, mf):
        pass

    def visit_simple_func(self, smp):
        pass

    def visit_increment(self, i):
        pass

    def visit_decrement(self, d):
        pass

    def visit_builtin_func(self, bltn):
        pass

    def visit_operand(self, op):
        pass

    pass