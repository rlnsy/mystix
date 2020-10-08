from .Command import Command
from ..Var import Var
from ..math_ast.MathFuncs import MathFuncs


class Trigger(Command):

    def __init__(self, var1: Var, math_funcs: MathFuncs):
        self.var1: Var = var1
        self.math_funcs: MathFuncs = math_funcs

