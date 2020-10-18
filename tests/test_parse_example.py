import unittest


from tests.util.example_ast import example_1
from tests.util import ast_equal
from mystix.ui.util import read_program_file
from mystix.language.tokenization import Tokenizer
from mystix.language.parsing import parse
from mystix.language.shared.ast import Program


class ExampleParseTests(unittest.TestCase):

    def test_parse_1(self):
        def run_compile(content: str) -> Program:
            return parse(Tokenizer(content).tokenize())
        p: Program = read_program_file(
            "tests/res/programs/example1", run_compile)
        #self.assertTrue(ast_equal(p, example_1()))
