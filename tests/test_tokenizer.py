import unittest as ut
from typing import List
from code.ui.util import read_program_file
from code.language.tokenization import tokenizer
from code.language.shared.ast import Program


class TestTokenizer(ut.TestCase):

    def test_tokenizer_1(self):
        def run_compile(content: str) -> List[str]:
            return tokenizer(content).tokenize()
        p: List[str] = read_program_file(
            "tests/res/programs/example1", run_compile)
        expected = ['<START>', ';', 'source ', '=', ' live ', 'remote', ' "www.coviddata.com/stream"', ';', 'map', ' source "case', 'date" ', 'to', ' ', 'number', ' date', ';', 'number', ' count ', '=', ' 0',
                    ';', 'on new data from', ' source count', '+', '+', ';', 'plot', ' xy date age ', 'called', ' age', 'graph', ';', 'plot', ' ', 'line xy', ' date ', 'log', '(count) ', 'called', ' cases', 'log', ';', '<END>', '']
        self.assertTrue(p, expected)
