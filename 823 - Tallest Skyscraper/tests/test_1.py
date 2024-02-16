from main import tallest_skyscraper
import unittest

tests = [
    {
        "args": [
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1],
            ]
        ],
        "return": 2,
    },
    {"args": [[[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]], "return": 4},
    {"args": [[[0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]]], "return": 4},
    {"args": [[[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]], "return": 3},
    {
        "args": [
            [
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1],
            ]
        ],
        "return": 5,
    },
    {"args": [[[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]], "return": 2},
]

class TestTallestSkyscraper(unittest.TestCase):
    def test_tallest_skyscraper(self):
        for test in tests:
            self.assertEqual(tallest_skyscraper(test["args"][0]), test["return"])