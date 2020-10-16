from unittest import TestCase
from tests.util.example_ast import simple_plot_example
from code.language.evaluation import Evaluator
from code.language.evaluation.errors import LanguageError
from code.language.evaluation.vars import UndefinedVariableError
from code.language.shared.primitives.values import FloatValue


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
        print("Testing undefined variable in Axis")
        program = simple_plot_example()
        e = Evaluator(graphics=False)
        code, err = e.evaluate(program)
        self.assertNotEqual(0, code)
        self.assertTrue(isinstance(err, UndefinedVariableError))

    """
    FIXME: running two tests consecutively with graphics enabled 
    creates seg-faults and QT errors
    """

    def test_plot_manual_define(self):
        """
        Should successfully create a plot and update with
        a constant value
        """
        print("Testing hard-coded variable value")
        program = simple_plot_example()
        e = Evaluator(graphics=False)
        e.env.extend('t', FloatValue(0.5))
        code, err = e.evaluate(program)
        self.assertEqual(0, code)

    def test_plot_manual_define_2(self):
        """
        Should successfully create a plot and update with
        a constant value
        """
        print("Testing hard-coded variable value 2")
        program = simple_plot_example()
        e = Evaluator(graphics=True)
        e.env.extend('t', FloatValue(1.0))
        code, err = e.evaluate(program)
        self.assertEqual(0, code)
