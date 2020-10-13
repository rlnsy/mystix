
import unittest as ut
import code.language.tokenization
from typing import List
from code.ui.util import read_program_file
from code.language.tokenization import tokenizer
from code.language.shared.ast import Program


class TestTokenizer(ut.TestCase):

    def test_tokenizer_1(self):
        def run_compile(content: str) -> List[str]:
            return tokenizer(content).tokenize
        p: List[str] = read_program_file(
            "tests/res/programs/example1", run_compile)
        res = ['<START>', ';', 'source', '=', 'live', 'remote', '"www.coviddata.com/stream"', ';', 'map',
               'source', '"case_date"', 'to', 'number', 'date', ';', 'number', 'count', '=', '0', ';',
               'on new data from', 'source', 'count++', ';', 'plot', 'xy', 'date', 'age', 'called', 'age_graph', ';',
               'plot', 'line', 'xy', 'date', 'log', '(', 'count', ')', 'called', 'cases_log', ';', '<END>']
        self.assertTrue(p, res)

    def test_tokenizer_2(self):
        def run_compile(content: str) -> List[str]:
            return tokenizer(content).tokenize
        p: List[str] = read_program_file(
            "tests/res/programs/example2", run_compile)
        res = ['<START>', ';', 'source', '=', 'static', 'remote', '"http://winterolympicsmedals.com/medals.csv"',
               ';', 'map', 'source', '"Year"', 'to', 'number', 'year', ';', 'map', 'source', '"Medal"', 'to', 'number',
               'medal', ';', 'plot', 'xy', 'year', 'medal', 'called', 'medal_graph', '<END>']
        self.assertTrue(p, res)

    def test_tokenizer_3(self):
        def run_compile(content: str) -> List[str]:
            return tokenizer(content).tokenize
        p: List[str] = read_program_file(
            "tests/res/programs/example3", run_compile)
        res = ['<START>', ';', 'source', '=', 'static', 'remote', '"http://winterolympicsmedals.com/medals.csv"',
               ';', 'map', 'source', '"Year"', 'to', 'number', 'year', ';', 'map', 'source', '"Medal"', 'to', 'number',
               'medal', ';', 'number', 'shortyear', '=', 'year', '-', '1900', ';', 'number', 'addyear', '=', 'year',
               '+', '50', ';', 'number', 'timesyear', '=', 'year', '*', '10', ';', 'number', 'divyear', '=', 'year',
               '/', '100', ';', 'number', 'sinyear', '=', 'sin(year)', ';', 'number', 'cosyear', '=', 'cos(year)', ';',
               'number', 'expyear', '=', 'exp(year)', ';', 'number', 'sqyear', '=', 'year', '^', '2', ';', 'number',
               'thing', '=', '2000', ';', 'thing--', ';', 'binary', 'bin', '=', 'true', ';', 'binary', 'bin2', '=',
               'false', ';', 'plot', 'xy', 'cos(year)', 'medal', 'called', 'cos_medal_graph', ';', '<END>']
        self.assertTrue(p, res)
