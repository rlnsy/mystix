from .evaluator import Evaluator
from code.language.shared import ast
from code.language.shared.primitives.misc import ReportingMode
from tests.util.example_ast import example_1


def run():
    e = Evaluator()
    p = ast.Program(
        ast.Body([
            ast.Loader(ast.Var("source"),
                       ast.Source(ast.Reporting(ReportingMode.LIVE),
                                  "https://covid-api.com/api/reports")),
            ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                "count"))])),
        ]))
    #p = example_1()
    code, err = e.evaluate(p)
