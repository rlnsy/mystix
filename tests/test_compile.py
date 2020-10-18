import unittest
from typing import List

from mystix.language.shared.ast import Program
from mystix.language.parsing import Parser
from mystix.language.tokenization import Tokenizer, TokenizationError
from mystix.language.evaluation import Evaluator


class CompilePipelineTests(unittest.TestCase):
    """
    Test tokenization through evaluation
    useful right now for validating function stubs
    """

    def test(self):
        content = "NOT A REAL PROGRAM"
        try:
            t = Tokenizer(content)
            t.tokenize()
            program: Program = Parser(t).parseProgram()
            result: int = Evaluator(graphics=False).evaluate(program, duration=5000)
            self.fail()
        except TokenizationError:
            pass
