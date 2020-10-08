from .Command import Command
from ..Var import Var
from ..Source import Source


class Loader(Command):
    def __init__(self, name: Var, source: Source):
        self.name: Var = name
        self.source: Source = source
