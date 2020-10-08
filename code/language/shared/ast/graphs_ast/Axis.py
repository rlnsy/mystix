from ..Node import Node
from ..Var import Var
from ..math_ast.MathFuncs import Func


class Axis(Node):
    pass


class VarAxis(Axis):

    def __init__(self, v: Var):
        self.var = Var


class FuncAxis(Axis):

    def __init__(self, f: Func):
        self.fun = f

