import unittest as ut
<<<<<<< HEAD


class TestExample(ut.TestCase):

    # def test_tokenize(self):

    def test_true(self):
        self.assertTrue(True)
=======
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
>>>>>>> 67863dccb530fcbc962c401b1aa9709548410896
