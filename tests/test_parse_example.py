import unittest


from tests.util.example_ast import EXAMPLE_1
from tests.util import ast_equal
from code.ui.util import read_program_file
from code.language.tokenization import tokenize
from code.language.parsing import parse
from code.language.shared.ast import Program


class ExampleParseTests(unittest.TestCase):

    def test_example_1(self):
        def run_compile(content: str) -> Program:
            return parse(tokenize(content))
        p: Program = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(ast_equal(p, EXAMPLE_1))
