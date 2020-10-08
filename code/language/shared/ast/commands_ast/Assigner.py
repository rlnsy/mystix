from .Command import Command
from ..Value import Value
from ..Declare import Declare


class Assigner(Command):

    def __init__(self, decl: Declare, value: Value):
        self.decl = Declare
        self.value: Value = value

