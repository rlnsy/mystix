from .Node import Node
from .Body import Body


class Program(Node):
    """
    Represents a program. This contains no additional fields other than
    the program body but is kept here for consistency with the Grammar
    """
    def __init__(self, b: Body):
        self.body: Body = b
