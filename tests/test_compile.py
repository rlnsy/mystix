import unittest
from typing import List

from mystix.language.shared.ast import Program
from mystix.language.evaluation.errors import LanguageError
from mystix.language.tokenization import Tokenizer
from mystix.language.parsing import parse
from mystix.language.evaluation import Evaluator


class CompilePipelineTests(unittest.TestCase):
    """
    Test tokenization through evaluation
    useful right now for validating function stubs
    """

    def test(self):
        content = "NOT A REAL PROGRAM"
        try:
            tokens: List[str] = Tokenizer(content).tokenize()
            program: Program = parse(tokens)
            result: int = Evaluator(graphics=False).evaluate(program, duration=5000)
            print(result)
        except LanguageError:
            self.fail()
