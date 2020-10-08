from .Node import Node


class Var(Node):
    def __init__(self, name: str):
        self.name = name
