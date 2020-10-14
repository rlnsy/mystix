from .Node import Node
from code.language.shared.primitives.misc import ReportingMode
from code.language.shared.ast.visitor import Visitor


class Reporting(Node):

    def __init__(self, mode: ReportingMode):
        self.mode = mode

    def accept(self, v: Visitor):
        return v.visit_reporting(self)
