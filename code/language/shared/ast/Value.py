from .Node import Node
from code.language.shared.primitives import ConcreteValue
from code.language.shared.ast.visitor import Visitor


class Value(Node):
    def __init__(self, v: ConcreteValue):
        self.value = v
        

    def accept(self, v: Visitor):
        return v.visit_value(self)

    pass
