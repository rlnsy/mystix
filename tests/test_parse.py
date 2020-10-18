
import unittest as ut
from typing import List
from code.ui.util import read_program_file
from code.language.tokenization.tokenizer import Tokenizer, TokenizationError
from code.language.parsing.parser import Parser
from code.language.shared.ast import *
from code.language.shared.primitives import *

class TestParse(ut.TestCase):

    def test_program(self):
        tokens, parser = self.setup("parse_program")
        res = parser.parseProgram()
        commands = res.body.commands
        self.assertEqual(commands[0].graph.graph, 'line_xy')
        self.assertEqual(commands[0].x.var.name, 'x')
        self.assertEqual(commands[0].y.fun.fun, 'log')
        self.assertEqual(commands[0].graph_name, 'line')
        self.assertEqual(commands[1].var1.name, 'triggerVar')
        self.assertEqual(len(commands[1].math_funcs.mth_func_lst), 2)
        self.assertEqual(commands[1].math_funcs.mth_func_lst[0].impacted_var.name, 'triggerVar')
        self.assertEqual(commands[1].math_funcs.mth_func_lst[1].impacted_var.name, 'triggerVar')
        self.assertEqual(commands[1].math_funcs.mth_func_lst[1].op.op, '+=')
        self.assertEqual(commands[1].math_funcs.mth_func_lst[1].rhs.value, '1')
        self.assertEqual(commands[2].decl.type.type, 'category')
        self.assertEqual(commands[2].decl.var.name, 'A')
        self.assertEqual(commands[2].value.value, '123456')


    def test_loader(self):
        tokens, parser = self.setup("parse_loader")
        res = parser.parseLoader()
        self.assertEqual(res.name.name, "x")
        self.assertEqual(res.source.url, "www.coviddata.com/stream")
    
    def test_fast_func(self):
        tokens, parser = self.setup("parse_fast_func")
        res = parser.parseFastFunc()
        self.assertEqual(res.impacted_var.name, 'x')
        self.assertIsInstance(res, Increment)

    def test_simp_func(self):
        tokens, parser = self.setup("parse_simp_func")
        res = parser.parseFunc(tokens)
        self.assertEqual(res.impacted_var.name, 'x')
        self.assertEqual(res.op.op, '+=')
        self.assertIsInstance(res, SimpleFunc)
    
    def test_mapper(self):
        tokens, parser = self.setup("parse_mapper")
        res = parser.parseMapper()
        self.assertEqual(res.src.name, 'testVar')
        self.assertEqual(res.tbl_field, 'testingAxis')
        self.assertEqual(res.decl.type.type, 'category')
        self.assertEqual(res.decl.var.name, 'A')

    def test_assigner(self):
        tokens, parser = self.setup("parse_assigner")
        res = parser.parseAssigner()
        self.assertEqual(res.decl.type.type, 'category')
        self.assertEqual(res.decl.var.name, 'A')
        self.assertEqual(res.value.value, '123456')
    
    def test_math_funcs(self):
        tokens, parser = self.setup("parse_math_funcs")
        res = parser.parseMathFuncs()
        self.assertEqual(len(res.mth_func_lst), 3)
        self.assertIsInstance(res.mth_func_lst[0], Increment)
        self.assertIsInstance(res.mth_func_lst[1], SimpleFunc)
        self.assertIsInstance(res.mth_func_lst[2], BuiltinFunc)

    def test_trigger(self):
        tokens, parser = self.setup("parse_trigger")
        res = parser.parseTrigger()
        self.assertEqual(res.var1.name, 'triggerVar')
        self.assertEqual(len(res.math_funcs.mth_func_lst), 2)
        self.assertEqual(res.math_funcs.mth_func_lst[0].impacted_var.name, 'triggerVar')
        self.assertEqual(res.math_funcs.mth_func_lst[1].impacted_var.name, 'triggerVar')
        self.assertEqual(res.math_funcs.mth_func_lst[1].op.op, '+=')
        self.assertEqual(res.math_funcs.mth_func_lst[1].rhs.value, '1')
    
    def test_plotter(self):
        tokens, parser = self.setup("parse_plotter")
        res = parser.parsePlotter()
        self.assertEqual(res.graph.graph, 'line_xy')
        self.assertEqual(res.x.var.name, 'x')
        self.assertEqual(res.y.fun.fun, 'log')
        self.assertEqual(res.graph_name, 'line')


    def setup(self, input = None):
        def run_compile(content: str) -> Tokenizer:
            tk = Tokenizer(content)
            tk.tokenize()
            return tk
        if (input is not None):
            tk = read_program_file(f"tests/res/programs/{input}", run_compile)
        else:
            tk = read_program_file("tests/res/programs/example1", run_compile)
        print("GOT TOKENS")
        tokens = tk.tokens
        print(tokens)
        parser = Parser(tk)
        return tokens, parser