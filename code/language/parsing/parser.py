from typing import List

from code.language.shared.ast import *
from code.language.shared.primitives import *
from code.language.tokenization import tokenizer

class Parser:
    operators = ['+', '-', '*', '/', '^']
    bltn = ['log', 'sin', 'cos', 'exp']

    def __init__(self, tokenizer: tokenizer):
        self.tokenizer = tokenizer

    def parseProgram(self):
        commands = []
        while(self.tokenizer.more_tokens()):
            command = self.parseCommand()
            commands.append(command)
        return Program(Body(commands))
    
    def parseCommand(self):
        next_token = self.tokenizer.check_next()
        command = None
        if (next_token == "map"):
            command = self.parseMapper()
        elif (next_token == "on new data from"):
            command = self.parseTrigger()
        elif (next_token == "plot"):
            command = self.parsePlotter()
        # Line is either Loader or Assigner
        line = self.tokenizer.get_line()
        if ("remote" in line):
            command = self.parseLoader()
        elif ("=" in line and "remote" not in line):
            command = self.parseAssigner()
        if (self.tokenizer.check_next() in ['\n', ';']):
            self.tokenizer.get_next()
        return command
    
    def parseLoader(self):
        var = self.parseVar()
        self.tokenizer.get_and_check_next("=")
        source = self.parseSource()
        return Loader(var, source)

    def parseMapper(self):
        self.tokenizer.get_and_check_next("map")
        var = Var(self.tokenizer.get_next())
        map_from = str(self.tokenizer.get_next())
        self.tokenizer.get_and_check_next("to")
        declare = self.parseDeclare()
        return Mapper(var, map_from, declare)
    
    def parseDeclare(self):
        var_type = Type(self.tokenizer.get_next())
        var = self.parseVar()
        return Declare(var_type, var)

    def parseAssigner(self):
        declare = self.parseDeclare()
        self.tokenizer.get_and_check_next("=")
        value = self.parseValue()
        return Assigner(declare, value)

    def parseTrigger(self):
        self.tokenizer.get_and_check_next("on new data from")
        var = self.parseVar()
        math_funcs = self.parseMathFuncs()
        return Trigger(var, math_funcs)

    def parsePlotter(self):
        self.tokenizer.get_and_check_next("plot")
        graph = self.parseGraph()
        x_axis = self.parseAxis()
        y_axis = self.parseAxis()
        self.tokenizer.get_and_check_next("called")
        name = self.tokenizer.get_next()
        return Plotter(graph, x_axis, y_axis, name)

    def parseSource(self):
        reporting = self.parseReporting()
        self.tokenizer.get_and_check_next("remote")
        url = self.tokenizer.get_next
        return Source(reporting, url)

    def parseMathFuncs(self):
        functions = []
        line = self.tokenizer.get_line()
        functions.append(self.parseFunc(line))
        next_token = self.tokenizer.get_next()
        while(next_token not in ['\n', ';'] and next_token == ','):
            functions.append(self.parseFunc(line))
            next_token = self.tokenizer.get_next()
        return MathFuncs(functions)
    
    def parseAxis(self):
        line = self.tokenizer.get_line()
        if(len(line) == 1):
            return VarAxis(self.tokenizer.get_next())
        elif self.isMathFunc(line):
            func = self.parseFunc(line)
            return FuncAxis(func)
        return Axis()

    def parseFunc(self, line):
        if (self.isFastFunc(line)):
            return self.parseFastFunc()
        elif (self.isSimpFunc(line)):
            return self.parseSimpFunc()
        elif (self.isBltnFunc(line)):
            return self.parseBltnFunc()

        return None

    def parseSimpFunc(self):
        var = Var(self.tokenizer.get_next())
        op = Operand(self.tokenizer.get_next())
        value = Value(self.tokenizer.get_next())
        return SimpleFunc(var, op, value)
    
    def parseFastFunc(self):
        token = self.tokenizer.get_next()
        var = token[:-2]
        operator = token[-2:]
        return FastFunc(var, operator)
    
    def parseBltnFunc(self):
        op = self.tokenizer.get_next()
        var = self.tokenizer.get_next()
        return 

    def parseGraph(self):
        return Graph(self.tokenizer.get_next())

    def parseReporting(self):
        return Reporting(self.tokenizer.get_next())

    def parseVar(self):
        return Var(self.tokenizer.get_next())

    def parseValue(self):
        return Value(self.tokenizer.get_next())

    def parseType(self):
        return Type(self.tokenizer.get_next())

    def isSep(self, input: str) -> bool:
        if (input == ';' or input == '\n'):
            return True
        return False

    def isMathFunc(self, line):
        if (self.isSimpFunc(line) or self.isFastFunc(line)):
            return True
        return False

    def isFastFunc(self, line):
        if (len(line) == 1 and ('++' in line[0] or '--' in line[0])):
            return True
        return False

    def isSimpFunc(self, line):
        if (len(line) == 3 and line[1] in self.operators):
            return True
        return False

    def isBltnFunc(self, line):
        if (len(line) == 2 and line[0] in self.bltn):
            return True
        return False