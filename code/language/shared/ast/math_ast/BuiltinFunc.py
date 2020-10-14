from .Func import Func
from ..Var import Var
from code.language.shared.primitives.numerical import NumFunction
from code.language.shared.ast.visitor import Visitor


class BuiltinFunc(Func):

    def __init__(self, fun: NumFunction, x: Var):
        self.fun: NumFunction = fun
        self.input: Var = x

    def accept(self, v: Visitor):
        return v.visit_builtin_func(self)
