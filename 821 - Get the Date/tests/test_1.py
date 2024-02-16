from main import get_day
import unittest

tests = [
    {"args": ["09/04/2016"], "return": "Sunday"},
    {"args": ["06/08/2012"], "return": "Friday"},
    {"args": ["12/08/2011"], "return": "Thursday"},
    {"args": ["08/13/2019"], "return": "Tuesday"},
    {"args": ["12/07/2016"], "return": "Wednesday"},
]


class TestGetDay(unittest.TestCase):
    def test_get_day(self):
        for test in tests:
            self.assertEqual(get_day(*test["args"]), test["return"])
