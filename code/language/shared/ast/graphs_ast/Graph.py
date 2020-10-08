from ..Node import Node
from code.language.shared.primitives import ConcreteGraph


class Graph(Node):

    def __init__(self, g: ConcreteGraph):
        self.graph = g
