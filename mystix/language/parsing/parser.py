from typing import Optional


from mystix.language.shared.ast import *
from mystix.language.tokenization import Tokenizer


class ParseError(Exception):
    pass


class Parser:
    operators = ['+=', '-=', '*=', '/=', '^=']
    bltn = ['log', 'sin', 'cos', 'exp']

    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer

    def parseProgram(self) -> Program:
        commands = []
        self.tokenizer.get_and_check_next("program:")
        self.tokenizer.get_and_check_next(";")
        while(self.tokenizer.more_tokens() and self.tokenizer.check_next() != "start!"):
            command = self.parseCommand()
            commands.append(command)
        self.tokenizer.get_and_check_next("start!")
        return Program(Body(commands))
    
    def parseCommand(self) -> Command:
        next_token = self.tokenizer.check_next()
        command: Optional[Command] = None
        if (next_token == "map"):
            print("Parsing Map")
            command = self.parseMapper()
        elif (next_token == "observe"):
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
        if command is not None:
            return command
        else:
            raise ParseError("Could not determine command")
    
    def parseLoader(self) -> Loader:
        var = self.parseVar()
        self.tokenizer.get_and_check_next("=")
        source = self.parseSource()
        return Loader(var, source)

    def parseMapper(self) -> Mapper:
        self.tokenizer.get_and_check_next("map")
        self.tokenizer.get_and_check_next("\(")
        var = Var(self.tokenizer.get_next())
        self.tokenizer.get_and_check_next("\)")
        map_from = self.parseString()
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
        self.tokenizer.get_and_check_next("observe")
        self.tokenizer.get_and_check_next("\(")
        var = self.parseVar()
        self.tokenizer.get_and_check_next("\)")
        self.tokenizer.get_and_check_next("do")
        math_funcs = self.parseMathFuncs()
        return Trigger(var, math_funcs)

    def parsePlotter(self) -> Plotter:
        self.tokenizer.get_and_check_next("plot")
        graph = self.parseGraph()
        self.tokenizer.get_and_check_next("\(")
        x_axis = self.parseAxis(',')
        print("X AXIS GOTTEN")
        self.tokenizer.get_and_check_next(',')
        print("COMMA CONFIRMED")
        y_axis = self.parseAxis(')')
        self.tokenizer.get_and_check_next("\)")
        self.tokenizer.get_and_check_next("titled")
        name = self.parseString()
        return Plotter(graph, x_axis, y_axis, name)

    def parseSource(self) -> Source:
        self.tokenizer.get_and_check_next("remote")
        self.tokenizer.get_and_check_next("\(")
        self.tokenizer.get_and_check_next("\"")
        url = self.tokenizer.get_next()
        self.tokenizer.get_and_check_next("\"")
        self.tokenizer.get_and_check_next("\)")
        return Source(url)

    def parseMathFuncs(self) -> MathFuncs:
        functions = []
        line = self.tokenizer.get_line(',')
        print(line)
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
        func: Optional[Func] = None
        if (self.isFastFunc(line)):
            func = self.parseFastFunc()
        elif (self.isSimpFunc(line)):
            func = self.parseSimpFunc()
        elif (self.isBltnFunc(line)):
            func = self.parseBltnFunc()
        print(func)
        print(self.tokenizer.check_next())
        if func is not None:
            return func
        else:
            raise ParseError("Could not determine function")

    def parseSimpFunc(self) -> SimpleFunc:
        var = Var(self.tokenizer.get_next())
        op = self.tokenizer.get_next()
        op += self.tokenizer.get_next()
        op = Operand(op)
        value = Value(self.tokenizer.get_next())
        return SimpleFunc(var, op, value)
    
    def parseFastFunc(self) -> FastFunc:
        token = self.tokenizer.get_next()
        var = Var(token[:-2])
        operator = token[-2:]
        if operator == '++':
            return Increment(var)
        else:
            return Decrement(var)
    
    def parseBltnFunc(self) -> BuiltinFunc:
        op = self.tokenizer.get_next()
        self.tokenizer.get_and_check_next("\(")
        var = self.tokenizer.get_next()
        self.tokenizer.get_and_check_next("\)")
        return BuiltinFunc(op, var)

    def parseString(self) -> str:
        self.tokenizer.get_and_check_next('"')
        string_token = ''
        while(self.tokenizer.check_next() != '"'):
            string_token += self.tokenizer.get_next()
        self.tokenizer.get_and_check_next('"')
        return string_token

    def parseGraph(self) -> Graph:
        return Graph(self.tokenizer.get_next())

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
        if (len(line) == 1 and line[0][-2:] in ops):
            return True
        return False

    def isSimpFunc(self, line):
        if (len(line) == 4 and str(line[1] + line[2]) in self.operators):
            return True
        return False

    def isBltnFunc(self, line):
        if (line[0] in self.bltn):
            return True
        return False
