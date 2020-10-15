import unittest


from tests.util.example_ast import example_1
from tests.util import ast_equal
from code.ui.util import read_program_file
from code.language.tokenization.tokenizer import tokenizer
from code.language.parsing import Parser
from code.language.shared.ast import Program


class ExampleParseTests(unittest.TestCase):

    def test_parse_1(self):
        def run_compile(content: str) -> Program:
            return Parser(tokenizer(content)).parseProgram()
        p: Program = read_program_file("tests/res/programs/example1", run_compile)
        # self.assertTrue(ast_equal(p, example_1()))
