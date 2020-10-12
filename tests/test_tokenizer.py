import unittest as ut
from typing import List
from tests.util.example_ast import example_1
from tests.util import ast_equal
from code.ui.util import read_program_file
from code.language.tokenization import tokenize
from code.language.shared.ast import Program

class TestTokenizer(ut.TestCase):

    def test_tokenizer_1(self):
        def run_compile(content: List[str]) -> Program:
            return tokenize(content)
        p: Program = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(ast_equal(p, example_1()))
