from unittest import TestCase
from tests.util.example_ast import simple_plot_example
from code.language.evaluation import Evaluator
from code.language.evaluation.errors import LanguageError
from code.language.evaluation.vars import UndefinedVariableError


class GraphicsEvaluationTests(TestCase):

    """
    tests portions of evaluator with graphical side-effects
    This test should be ignored if graphics do not work on
    your system.
    """

    def test_plot_undefined_axes(self):
        """
        Should briefly create a plot then error
        """
        program = simple_plot_example()
        e = Evaluator(graphics=True)
        code, err = e.evaluate(program)
        self.assertNotEqual(0, code)
        self.assertTrue(isinstance(err, UndefinedVariableError))
