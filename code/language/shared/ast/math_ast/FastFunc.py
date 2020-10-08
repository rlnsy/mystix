from .Func import Func
from ..Var import Var


class FastFunc(Func):
    def __init__(self, impacted_var: Var):
        self.impacted_var: Var = impacted_var


class Increment(FastFunc):
    pass


class Decrement(FastFunc):
    pass
