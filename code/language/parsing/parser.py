from typing import List

from code.language.shared.ast import *
from code.language.shared.primitives import *
from code.language.tokenization import tokenizer

class Parser:
    operators = ['+', '-', '*', '/', '^']
    bltn = ['log', 'sin', 'cos', 'exp']

    def __init__(self, tokenizer: tokenizer):
        self.tokenizer = tokenizer

    def parseProgram(self) -> Program:
        commands = []
        self.tokenizer.get_and_check_next("<START>")
        self.tokenizer.get_and_check_next(";")
        while(self.tokenizer.more_tokens() and self.tokenizer.check_next() != "<END>"):
            command = self.parseCommand()
            commands.append(command)
        self.tokenizer.get_and_check_next("<END>")
        return Program(Body(commands))
    
    def parseCommand(self) -> Command:
        next_token = self.tokenizer.check_next()
        command = None
        if (next_token == "map"):
            print("Parsing Map")
            command = self.parseMapper()
        elif (next_token == "on"):
            print("Parsing Trigger")
            command = self.parseTrigger()
        elif (next_token == "plot"):
            print("Parsing Plotter")
            command = self.parsePlotter()
        # Line is either Loader or Assigner
        line = self.tokenizer.get_line()
        if ("remote" in line):
            print('Parsing Loader')
            command = self.parseLoader()
        elif ("=" in line and "remote" not in line):
            print('Parsing Assigner')
            command = self.parseAssigner()
        while (self.tokenizer.check_next() in ['\n', ';']):
            self.tokenizer.get_next()
        return command
    
    def parseLoader(self) -> Loader:
        var = self.parseVar()
        self.tokenizer.get_and_check_next("=")
        source = self.parseSource()
        return Loader(var, source)

    def parseMapper(self) -> Mapper:
        self.tokenizer.get_and_check_next("map")
        var = Var(self.tokenizer.get_next())
        map_from = str(self.tokenizer.get_next())
        self.tokenizer.get_and_check_next("to")
        declare = self.parseDeclare()
        return Mapper(var, map_from, declare)
    
    def parseDeclare(self) -> Declare:
        var_type = Type(self.tokenizer.get_next())
        var = self.parseVar()
        return Declare(var_type, var)

    def parseAssigner(self) -> Assigner:
        declare = self.parseDeclare()
        self.tokenizer.get_and_check_next("=")
        value = self.parseValue()
        return Assigner(declare, value)

    def parseTrigger(self) -> Trigger:
        self.tokenizer.get_and_check_next("on")
        self.tokenizer.get_and_check_next("new")
        self.tokenizer.get_and_check_next("data")
        self.tokenizer.get_and_check_next("from")
        var = self.parseVar()
        math_funcs = self.parseMathFuncs()
        return Trigger(var, math_funcs)

    def parsePlotter(self) -> Plotter:
        self.tokenizer.get_and_check_next("plot")
        graph = self.parseGraph()
        x_axis = self.parseAxis(',')
        print("X AXIS GOTTEN")
        self.tokenizer.get_and_check_next(',')
        print("COMMA CONFIRMED")
        y_axis = self.parseAxis('titled')
        self.tokenizer.get_and_check_next("titled")
        name = self.tokenizer.get_next()
        return Plotter(graph, x_axis, y_axis, name)

    def parseSource(self) -> Source:
        reporting = self.parseReporting()
        self.tokenizer.get_and_check_next("remote")
        url = ''
        while(self.tokenizer.check_next() != ';'):
            url += self.tokenizer.get_next()
        return Source(reporting, url)

    def parseMathFuncs(self) -> MathFuncs:
        functions = []
        line = self.tokenizer.get_line(',')
        functions.append(self.parseFunc(line))
        next_token = self.tokenizer.get_next()
        while(next_token not in ['\n', ';'] and next_token == ','):
            line = self.tokenizer.get_line(',')
            functions.append(self.parseFunc(line))
            next_token = self.tokenizer.get_next()
        return MathFuncs(functions)
    
    def parseAxis(self, endline = ',') -> Axis:
        line = self.tokenizer.get_line(endline)
        print(line)
        if(len(line) == 1):
            return VarAxis(Var(self.tokenizer.get_next()))
        elif self.isMathFunc(line):
            func = self.parseFunc(line)
            return FuncAxis(func)
        return Axis()

    def parseFunc(self, line) -> Func:
        if (self.isFastFunc(line)):
            return self.parseFastFunc()
        elif (self.isSimpFunc(line)):
            return self.parseSimpFunc()
        elif (self.isBltnFunc(line)):
            return self.parseBltnFunc()

        return None

    def parseSimpFunc(self) -> SimpleFunc:
        var = Var(self.tokenizer.get_next())
        op = Operand(self.tokenizer.get_next())
        value = Value(self.tokenizer.get_next())
        return SimpleFunc(var, op, value)
    
    def parseFastFunc(self) -> FastFunc:
        var = Var(self.tokenizer.get_next())
        operator = self.tokenizer.get_next()
        operator += self.tokenizer.get_next()
        if operator == '++':
            return Increment(var)
        else:
            return Decrement(var)
    
    def parseBltnFunc(self) -> BuiltinFunc:
        op = self.tokenizer.get_next()
        var = self.tokenizer.get_next()
        return BuiltinFunc(op, var)

    def parseGraph(self) -> Graph:
        if self.tokenizer.check_next() == 'line':
            graph = self.tokenizer.get_next() + ' '
            graph += self.tokenizer.get_next()
            return Graph(graph)
        return Graph(self.tokenizer.get_next())

    def parseReporting(self) -> Reporting:
        return Reporting(self.tokenizer.get_next())

    def parseVar(self) -> Var:
        return Var(self.tokenizer.get_next())

    def parseValue(self) -> Value:
        return Value(self.tokenizer.get_next())

    def parseType(self) -> Type:
        return Type(self.tokenizer.get_next())

    def isSep(self, input: str) -> bool:
        if (input == ';' or input == '\n'):
            return True
        return False

    def isMathFunc(self, line):
        if (self.isSimpFunc(line) or self.isFastFunc(line) or self.isBltnFunc(line)):
            return True
        return False

    def isFastFunc(self, line):
        ops = ['++', '-']
        if (len(line) == 3 and (line[1] + line[2] in ops)):
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
