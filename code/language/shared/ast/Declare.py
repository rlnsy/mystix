from .Node import Node
from .Type import Type
from .Var import Var


class Declare(Node):

    def __init__(self, t: Type, v: Var):
        self.type = t
        self.var = v
