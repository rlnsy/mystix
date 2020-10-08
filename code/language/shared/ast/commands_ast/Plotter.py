from .Command import Command
from ..graphs_ast.Graph import Graph
from ..graphs_ast.Axis import Axis


class Plotter(Command):
    def __init__(self, graph: Graph, x_axis: Axis, y_axis: Axis, name: str):
        self.graph: Graph = graph
        self.x: Axis = x_axis
        self.y: Axis = y_axis
        self.graph_name: str = name

