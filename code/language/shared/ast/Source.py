from .Node import Node
from .Reporting import Reporting


class Source(Node):
    def __init__(self, reporting: Reporting, url: str):
        self.reporting: Reporting = reporting
        self.url: str = url
