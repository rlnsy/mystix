from typing import List

from code.language.shared.ast import *
from code.language.tokenization import tokenizer

class Parser:

    def __init__(self, tokenizer: tokenizer):
        self.tokenizer = tokenizer

    def parse(self, tokens: List[str]) -> Program:
        """
        PARSER
        """
        return Program(Body([]))  # stub

    def parseProgram(self ):
        return Program(Body(self []))

    def parseLoader(self):
        var = self.parseVar()
        tokenizer.get_and_check_next("=")
        source = self.parseSource()
        return Loader(var, source)

    def parseMapper(self):
        tokenizer.get_and_check_next("map")
        var = Var(tokenizer.get_next())
        map_from = str(tokenizer.get_next())
        tokenizer.get_and_check_next("to")
        declare = self.parseDeclare()
        return Mapper(var, map_from, declare)
    
    def parseDeclare(self):
        var_type = Type(tokenizer.get_next())
        var = self.parseVar()
        return Declare(var_type, var)

    def parseAssigner(self):
        delcare = self.parseDeclare()
        tokenizer.get_and_check_next("=")
        value = self.parseValue()
        return Assigner(declare, value)

    def parseTrigger(self):
        tokenizer.get_and_check_next("on new data from")
        var = self.parseVar()
        math_funcs = self.parseMathFuncs()
        return Trigger(var, math_funcs)

    def parseSource(self):
        reporting = self.parseReporting()
        tokenizer.get_and_check_next("remote")
        url = tokenizer.get_next
        return Source(reporting, url)

    def parseMathFuncs(self):
        # TODO: TEST
        functions = []
        functions.append(self.parseFunc())
        next_token = tokenizer.get_next()
        while(next_token not in ['\n', ';'] and next_token == ','):
            functions.append(self.parseFunc())
            next_token = tokenizer.get_next()
        return MathFuncs()
    
    def parseAxis(self):
        # TODO: 
        return Axis()

    def parseFunc(self):
        # TODO
        return Func()

    def parseGraph(self):
        # TODO
        return Graph()

    def parseReporting(self):
        return Reporting(tokenizer.get_next())

    def parseVar(self):
        return Var(tokenizer.get_next())

    def parseValue(self):
        return Value(tokenizer.get_next())

    def parseType(self):
        return Type(tokenizer.get_next())

    def isSep(self input: str) -> bool:
        if (self input == ';' or input == '\n'):
            return True
        return False
