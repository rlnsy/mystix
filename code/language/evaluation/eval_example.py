from .evaluator import Evaluator
from code.language.shared import ast
from code.language.shared.primitives.misc import ReportingMode
from tests.util.example_ast import example_1
from ..shared.primitives import Types
from ..shared.primitives.graphs import ScatterXYGraph, LineXYGraph
from ..shared.primitives.numerical import NumFunction
from ..shared.primitives.values import IntegerValue


def run():
    e = Evaluator(graphics=True)
    p = ast.Program(
            ast.Body([

                # source = live remote "https://covid-api.com/api/reports"
                ast.Loader(ast.Var("source"),
                                        ast.Source(ast.Reporting(ReportingMode.LIVE),
                                                   "https://covid-api.com/api/reports")),

                # map source "case_date" to number date
                ast.Mapper(ast.Var("source"), "confirmed",
                           ast.Declare(ast.Type(Types.NUMBER), ast.Var("confirmed"))),

                # number count = 0
                ast.Assigner(ast.Declare(ast.Type(Types.NUMBER), ast.Var("count")),
                             ast.Value(IntegerValue(0))),

                # on new data from source count++
                ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                    "count"))])),

                # plot xy date age called age_graph
                ast.Plotter(ast.Graph(LineXYGraph()),
                            ast.VarAxis(ast.Var("count")),
                            ast.VarAxis(ast.Var("confirmed")), "age_graph"),

            ]))
    code, err = e.evaluate(p)
