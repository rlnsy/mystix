from __future__ import annotations
from typing import TYPE_CHECKING as STATIC_CHECK
if STATIC_CHECK:
    from code.language.shared.ast import *
from code.language.shared.ast.visitor import Visitor
from code.language.shared.primitives import values, numerical
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

    def __init__(self):
        self.env = Environment()
        # maps a source name to a field mapping dict
        self.maps = defaultdict(lambda: {})
        # for source name provide a list of procedures to execute
        self.events = defaultdict(lambda: [])

    def evaluate(self, p: Program):
        return self.visit_program(p)

    def visit_program(self, p: Program):
        pass

    def visit_body(self, b: Body):
        pass
    
    def visit_loader(self, l: Loader):
        pass

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
        return self.env.set_val(n, a.value)

    def visit_trigger(self, t: Trigger):
        # TODO: source should be stored in environment
        self.events[t.var1.name].append(lambda: t.math_funcs.accept(self))

    def visit_plotter(self, pltr: Plotter):
        pass

    def visit_reporting(self, r: Reporting):
        pass

    def visit_var(self, v: Var):
        pass

    def visit_source(self, s: Source):
        pass

    def visit_type(self, t: Type):
        return t.type

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
