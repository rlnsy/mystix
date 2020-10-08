from .Node import Node
from code.language.shared.primitives.misc import ReportingMode


class Reporting(Node):

    def __init__(self, mode: ReportingMode):
        self.mode = mode
