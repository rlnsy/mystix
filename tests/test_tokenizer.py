import unittest as ut
from typing import List
from code.ui.util import read_program_file
from code.language.tokenization import tokenize
from code.language.shared.ast import Program

class TestTokenizer(ut.TestCase):

    def test_tokenizer_1(self):
        def run_compile(content: str) -> Program:
            return tokenize(content)
        p: Program = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p, str)

    def test_tokenizer_2(self):
        def run_compile(content: str) -> Program:
            return tokenize(content)
        p: Program = read_program_file("tests/res/programs/example2", run_compile)
        self.assertTrue(p, str)
