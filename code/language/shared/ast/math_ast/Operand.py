from ..Node import Node
from code.language.shared.primitives import ConcreteNumOp


class Operand(Node):

    def __init__(self, o: ConcreteNumOp):
        self.op = o
