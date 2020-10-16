from unittest import TestCase
from code.language.evaluation import Evaluator
from code.language.shared import ast
from code.language.shared.primitives.misc import ReportingMode
from code.targets.data.dataLoader import DataLoaderError


class LoaderEvaluationTests(TestCase):

    def test_duplicate_name(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source(ast.Reporting(ReportingMode.LIVE),
                                      "www.source.com")),
                ast.Loader(ast.Var("source"),
                           ast.Source(ast.Reporting(ReportingMode.LIVE),
                                      "www.source2.com")),
            ]))
        code, err = e.evaluate(p)
        self.assertNotEqual(0, code)
        self.assertTrue(isinstance(err, DataLoaderError))

    def test_invalid_host_no_trigger(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source(ast.Reporting(ReportingMode.LIVE),
                                      "https://covid-apiiii.com/api/reports")),
            ]))
        code, err = e.evaluate(p)
        self.assertNotEqual(0, code)
        self.assertTrue(isinstance(err, DataLoaderError))

    def test_invalid_host(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source(ast.Reporting(ReportingMode.LIVE),
                                      "https://covid-apiiii.com/api/reports")),
                ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                    "count"))])),
            ]))
        code, err = e.evaluate(p)
        self.assertNotEqual(0, code)
        self.assertTrue(isinstance(err, DataLoaderError))

    def test_valid_source(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source(ast.Reporting(ReportingMode.LIVE),
                                      "https://covid-api.com/api/reports")),
                ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                    "count"))])),
            ]))
        code, err = e.evaluate(p)
        self.assertEqual(0, code)
