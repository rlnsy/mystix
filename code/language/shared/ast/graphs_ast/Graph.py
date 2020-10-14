from ..Node import Node
from code.language.shared.primitives import ConcreteGraph
from code.language.shared.ast.visitor import Visitor


class Graph(Node):

    def __init__(self, g: ConcreteGraph):
        self.graph = g
        

    def accept(self, v: Visitor):
        return v.visit_graph(self)

    pass
