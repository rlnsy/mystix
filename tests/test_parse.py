import unittest


from tests.util.example_ast import example_1
from tests.util import ast_equal
from code.ui.util import read_program_file
from code.language.tokenization import tokenize
from code.language.parsing import parse
from code.language.shared.ast import Program


class ParseTests(unittest.TestCase):

    pass