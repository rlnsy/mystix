from ..Node import Node
from code.language.shared.primitives import ConcreteNumOp
from code.language.shared.ast.visitor import Visitor


class Operand(Node):

    def __init__(self, o: ConcreteNumOp):
        self.op = o
        pass

    def accept(self, v: Visitor):
        return v.visit_operand(self)
