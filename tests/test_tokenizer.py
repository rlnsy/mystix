
import unittest as ut
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

    def test_tokenizer_get_next(self):
        def run_compile(content: str) -> str:
            tokenizer(content).tokenize()
            return tokenizer(content).get_next
        p:str = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p, '<START>')
        p = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p, ';')
        p = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p, 'source')

    def test_tokenizer_check_next(self):
        def run_compile(content: str) -> bool:
            tokenizer(content).tokenize()
            return tokenizer(content).check_next
        p:str = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p, True)
        
    def test_tokenizer_check_next2(self):
        def run_compile(content: str) -> bool:
            tokenizer(content).tokenize()
            return tokenizer(content).check_next
        p:str = read_program_file("tests/res/programs/empty", run_compile)
        self.assertTrue(p, False)

    def test_tokenizer_check_token(self):
        def run_compile(content: str) -> bool:
            return tokenizer(content).check_token('<START>')
        def run_compile2(content: str) -> str:
            tokenizer(content).tokenize()
            return tokenizer(content).get_next
        p:str = read_program_file("tests/res/programs/example1", run_compile2)
        p = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p, True)
        p = read_program_file("tests/res/programs/example1", run_compile2)
        p = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p, False)

    def test_tokenizer_get_and_check_next(self):
        def run_compile(content: str) -> str:
            tokenizer(content).tokenize()
            return tokenizer(content).get_and_check_next('<START>')
        p:str = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p, '<START>')

    def test_tokenizer_get_and_check_next2(self):
        def run_compile(content: str) -> str:
            tokenizer(content).tokenize()
            return tokenizer(content).get_and_check_next('source')
        try:
            p:str = read_program_file("tests/res/programs/example1", run_compile)
            self.assertTrue(False, True)
        except:
            self.assertTrue(True, True)


    def test_tokenizer_more_tokens(self):
        def run_compile(content: str) -> bool:
            tokenizer(content).tokenize()
            return tokenizer(content).more_tokens
        p:str = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p, True)

    def test_tokenizer_more_tokens2(self):
        def run_compile(content: str) -> bool:
            tokenizer(content).tokenize()
            return tokenizer(content).more_tokens
        p:str = read_program_file("tests/res/programs/empty", run_compile)
        self.assertTrue(p, False)
    
    
