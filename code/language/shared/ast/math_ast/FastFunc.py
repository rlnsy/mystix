from .Func import Func
from ..Var import Var


class FastFunc(Func):
    def __init__(self, impacted_var: Var, operator: str):
        self.impacted_var: Var = impacted_var
        self.operator = operator


class Increment(FastFunc):
    pass


class Decrement(FastFunc):
    pass
