
import unittest as ut
from typing import List
from code.ui.util import read_program_file
from code.language.tokenization import tokenizer
from code.language.parsing.parser import Parser
from code.language.shared.ast import *
from code.language.shared.primitives import *

class TestParse(ut.TestCase):

    def test_loader(self):
        tokens, parser = self.setup("parse_loader")
        print(tokens)
        res = parser.parseLoader()
        print(res)
        self.assertEqual(res.name.name, "x")
        self.assertEqual(res.source.reporting.mode, "live")
        self.assertEqual(res.source.url, "www.coviddata.com/stream")
    
    def test_fast_func(self):
        tokens, parser = self.setup("parse_fast_func")
        res = parser.parseFastFunc()
        self.assertEqual(res.impacted_var.name, 'x')
        self.assertIsInstance(res, Increment)
    
    def test_mapper(self):
        # TODO: Test again after Adrian fixes tokenizer
        tokens, parser = self.setup("parse_mapper")
        res = parser.parseMapper()
        self.assertEqual(res.src.name, 'x')
        self.assertEqual(res.tbl_field, 'x-axis')
        self.assertEqual(res.decl.type.type, 'category')
        self.assertEqual(res.decl.var.name, 'A')

    def test_assigner(self):
        tokens, parser = self.setup("parse_assigner")
        res = parser.parseAssigner()
        self.assertEqual(res.decl.type.type, 'category')
        self.assertEqual(res.decl.var.name, 'A')
        self.assertEqual(res.value.value, '123456')

    def test_trigger(self):
        # TODO
        tokens, parser = self.setup("parse_trigger")
        res = parser.parseTrigger()
        self.assertEqual(res.var1.name, 'triggerVar')
        self.assertEqual(len(res.math_funcs.mth_func_lst), 2)
        self.assertEqual(res.math_funcs.mth_func_lst[0].var.name, 'triggerVar')
    
    def test_plotter(self):
        # TODO
        tokens, parser = self.setup("parse_plotter")
        res = parser.parsePlotter()
        self.assertTrue(true)


    def setup(self, input = None):
        def run_compile(content: str) -> List[str]:
            tk = tokenizer(content)
            return tk, tk.tokenize()
        if (input is not None):
            tk, tokens = read_program_file(f"tests/res/programs/{input}", run_compile)
        else:
            tk, tokens = read_program_file("tests/res/programs/example1", run_compile)
        print("GOT TOKENS")
        print(tokens)
        parser = Parser(tk)
        return tokens, parser