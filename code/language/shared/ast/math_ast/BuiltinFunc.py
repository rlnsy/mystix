from .Func import Func
from ..Var import Var
from code.language.shared.primitives.numerical import NumFunction


class BuiltinFunc(Func):

    def __init__(self, fun: NumFunction, x: Var):
        self.fun:NumFunction = fun
        self.input: Var = x
