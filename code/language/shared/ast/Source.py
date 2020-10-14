from .Node import Node
from .Reporting import Reporting
from code.language.shared.ast.visitor import Visitor


class Source(Node):
    def __init__(self, reporting: Reporting, url: str):
        self.reporting: Reporting = reporting
        self.url: str = url
        

    def accept(self, v: Visitor):
        return v.visit_source(self)

    pass