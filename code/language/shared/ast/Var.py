from .Node import Node
from ...evaluation.visitor import Visitor


class Var(Node):
    def __init__(self, name: str):
        self.name = name
        

    def accept(self, v: Visitor):
        return v.visit_var(self)

    pass