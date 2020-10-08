from typing import List

from .Node import Node
from .commands_ast.Command import Command


class Body(Node):
    """
    Program body
    """
    def __init__(self, cs: List[Command]):
        self.commands: List[Command] = cs
