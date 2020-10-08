from .Node import Node
from code.language.shared.primitives import ConcreteValue


class Value(Node):
    def __init__(self, v: ConcreteValue):
        self.value = v
