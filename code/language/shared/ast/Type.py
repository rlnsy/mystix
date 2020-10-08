from .Node import Node
from code.language.shared.primitives import Types


class Type(Node):

    def __init__(self, t: Types):
        self.type = t
