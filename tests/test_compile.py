import unittest
from typing import List

from code.language.shared.ast import Program
from code.language.evaluation.errors import LanguageError
from code.language.tokenization import tokenizer
from code.language.parsing import Parser
from code.language.evaluation import Evaluator


class CompilePipelineTests(unittest.TestCase):
    """
    Test tokenization through evaluation
    useful right now for validating function stubs
    """

    def test(self):
        content = "NOT A REAL PROGRAM"
        try:
            program: Program = Parser(tokenizer(content)).parseProgram()
            result: int = Evaluator().evaluate(program)
            print(result)
        except LanguageError:
            self.fail()
