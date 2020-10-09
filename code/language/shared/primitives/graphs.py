

class Graph:
    def equals(self, g) -> bool:
        return False


class LineXYGraph(Graph):
    def equals(self, g: Graph) -> bool:
        return isinstance(g, LineXYGraph)


class ScatterXYGraph(Graph):
    def equals(self, g: Graph) -> bool:
        return isinstance(g, ScatterXYGraph)
