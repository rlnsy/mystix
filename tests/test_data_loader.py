import unittest
from code.evaluation.dataLoader import load_data
import filecmp


class DataLoaderTests(unittest.TestCase):

    def test_run(self):
        load_data("http://winterolympicsmedals.com/medals.csv",
                  "tests/out/dataLoaderOutputActual.txt")
        self.assertTrue(filecmp.cmp('tests/res/dataLoaderOutputExpected.txt',
                                    'tests/out/dataLoaderOutputActual.txt'))
