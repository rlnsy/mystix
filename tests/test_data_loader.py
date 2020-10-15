import unittest
from code.targets.data import DataLoader, DataLoaderError
import filecmp
from typing import List


class DataLoaderTests(unittest.TestCase):

    # def test_run(self):
    #     load_data("http://winterolympicsmedals.com/medals.csv",
    #               "tests/out/dataLoaderOutputActual.txt")
    #     self.assertTrue(filecmp.cmp('tests/res/dataLoaderOutputExpected.txt',
    #                                 'tests/out/dataLoaderOutputActual.txt'))

    def test_not_exist(self):
        d = DataLoader()
        try:
            d.get_new("data")
            self.fail()
        except DataLoaderError:
            pass

    def test_register_already_exist(self):
        d = DataLoader()
        d.register_source("awkjlda", "data")
        try:
            d.register_source("awkjldadaw", "data")
            self.fail()
        except DataLoaderError:
            pass

    def test_get_new(self):
        d = DataLoader()
        d.register_source("mockurl", "mock_covid_api")
        data: List = d.get_new("mock_covid_api")
        self.assertTrue(len(data) > 0)  # assumed only for mock
        self.assertTrue('confirmed' in data[0])

    def test_multi_source(self):
        d = DataLoader()
        d.register_source("mockurl", "mock_covid_api")
        d.register_source("mockurl", "mock_covid_api_2")
        data: List = d.get_new("mock_covid_api")
        data2: List = d.get_new("mock_covid_api_2")
        self.assertEqual(data, data2)

    def test_multi_get(self):
        d = DataLoader()
        d.register_source("mockurl", "mock_covid_api")
        data: List = d.get_new("mock_covid_api")
        data2: List = d.get_new("mock_covid_api")
        self.assertNotEqual(data, data2)
