import csv, urllib.request, requests, json  # type: ignore
from typing import List


""" 
Mock hard-coded URL
This endpoint returns daily case reports.
"""
STUB_COMPATIBLE_URL = "https://covid-api.com/api/reports"


class DataLoaderError(Exception):
    pass


class MockDateGenerator:

    def __init__(self):
        self.year = 2020
        self.month = 3
        self.day = 1

    def get(self) -> str:
        date = "%d-%02d-%02d" % (self.year, self.month, self.day)
        self.day = self.day + 1
        if self.day > 28:
            self.month = self.month + 1
            self.day = 1
        if self.month > 12:
            self.year = self.year + 1
            self.month = 1
        return date


class DataSource:

    """
    Encapsulates a data source that updates over time
    """

    def __init__(self, url: str):
        self.url = url
        self.dates = MockDateGenerator()

    def get_new(self) -> List:
        """
        Returns a list of JSON-like dicts whose field names
        correspond to mappable headers
        Data url and format are hardcoded until we introduce
        features to match data appropriately
        simulates a stream by getting data for new dates each time
        """
        d: str = self.dates.get()
        req = requests.get(STUB_COMPATIBLE_URL, params={'date': d})
        res = req.text
        if req.status_code != 200:
            raise DataLoaderError("Could not fetch new data")
        with open("tmp/load_cache/api_response_%s.json" % d, "w") as cache:
            cache.write(res)
        obj = json.loads(res)
        return obj['data']


class DataLoader:

    def __init__(self):
        self.sources = {}

    def register_source(self, url: str, src_id: str):
        if src_id in self.sources:
            raise DataLoaderError("Source '%s' is already registered" % src_id)
        else:
            self.sources[src_id] = DataSource(url)

    def get_new(self, src_id: str) -> List:
        if src_id not in self.sources:
            raise DataLoaderError("Source '%s' does not exist" % src_id)
        else:
            s: DataSource = self.sources[src_id]
            return s.get_new()


# def load_data(url: str, file: str = None):
#     response = urllib.request.urlopen(url)
#     lines = [l.decode('utf-8') for l in response.readlines()]
#     data = csv.reader(lines)
#
#     if file is not None:
#         text_file = open(file, "w")
#
#     for row in data:
#         if file is not None:
#             text_file.write("[")
#             for s in row:
#                 text_file.write("'"+s+"', ")
#             text_file.write("]\n")
#
#     if file is not None:
#         text_file.close()
#
#     return data
