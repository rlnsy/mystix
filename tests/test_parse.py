
import unittest as ut
from typing import List
from code.ui.util import read_program_file
from code.language.tokenization import tokenizer
from code.language.parsing.parser import Parser
from code.language.shared.ast import Program

class TestParse(ut.TestCase):

    def test_loader(self):
        tokens, parser = self.setup("parse1")
        print(tokens)
        # res = parser.parseLoader()
        # print(res)
        self.assertTrue(True)

    def setup(self, input = None):
        def run_compile(content: str) -> List[str]:
            tk = tokenizer(content)
            return tk, tk.tokenize()
        if (input is not None):
            tk, tokens = read_program_file(f"tests/res/programs/{input}", run_compile)
        else:
            tk, tokens = read_program_file("tests/res/programs/example1", run_compile)
        print("GOT TOKENS")
        # parser = Parser(tk)
        return tokens, parser