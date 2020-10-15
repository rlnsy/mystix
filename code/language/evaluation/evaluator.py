from __future__ import annotations
from typing import TYPE_CHECKING as STATIC_CHECK
if STATIC_CHECK:
    from code.language.shared.ast import *
from code.language.shared.ast.visitor import Visitor
from code.language.shared.primitives import values, numerical
from code.targets.analysis.math import apply_fn, apply_op
from .errors import LanguageError
from .vars import Environment


class Evaluator(Visitor):
    # variable_table = {}
    # data = {}

    def __init__(self):
        self.env = Environment()

    # __operations = {
    #     "+": "__Sum",
    #     "-": "__Dif",
    #     "*": "__Mul",
    #     "/": "__Div",
    #     "^": "__Pow"
    # }

    def evaluate(self, p: Program):
        return self.visit_program(p)

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
        # try:
        #     # data_source = self.data[t.var]
        #     # implement Observer Pattern to watch for data updates
        # except:
        #     raise KeyError("Cannot run mathematics on invalid data")
        # else:
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

        # if smp.impacted_var not in self.variable_table:
        #     self.variable_table[smp.impacted_var.name] = 0
        
        # curr_val = self.variable_table[smp.impacted_var.name]
        # num = 0
        if isinstance(smp.rhs.value, values.NumericalValue):
            v: values.Value = self.env.get_val(smp.impacted_var.name)
            if isinstance(v, values.NumericalValue):
                operand = smp.op.accept(self)
                return apply_op(operand,v, smp.rhs.value)
            else:
                raise LanguageError("Simple Functions only accept numbers.")
        else:
            raise LanguageError("Simple Functions only accept numbers.")

        # self.variable_table[smp.impacted_var.name] = self.__calculate(curr_val, smp.op, num)
        pass

    def visit_increment(self, i: Increment):
        pass

    def visit_decrement(self, d: Decrement):
        pass

    def visit_builtin_func(self, bltn: BuiltinFunc):
        v: values.Value = self.env.get_val(bltn.input.name)
        if isinstance(v, values.NumericalValue):
            return apply_fn(bltn.fun, v)
        else:
            raise LanguageError("BuiltIn Functions only accept numbers.")

    def visit_operand(self, op: Operand) -> numerical.NumOp:
        return op.op

    # """
    # To call calculation methods dynamically using a dictionary.
    # Per this post:
    # https://stackoverflow.com/questions/16642145/how-to-dynamically-call-methods-within-a-class-using-method-name-assignment-to-a?lq=1
    # """
    # def __calculate(self, curr_val, op:Operand, rhs):
    #     func_name = self.__operations[op.op.value]
    #     func = getattr(self,func_name)
    #     return func(curr_val, rhs)

    # def __Sum(self, val1, val2):
    #     return val1 + val2

    # def __Dif(self, val1, val2):
    #     return val1 - val2

    # def __Mul(self, val1, val2):
    #     return val1 * val2

    # def __Div(self, val1, val2):
    #     if val1 == 0 or val2 == 0
    #         raise ZeroDivisionError("Cannot divide by 0!")
    #     return val1 / val2

    # def __Pow(self, val1, val2):
    #     return val1 ** val2