from main import snake_fill
import unittest

tests = [
    {"args": [3], "return": 3},
    {"args": [6], "return": 5},
    {"args": [900], "return": 19},
    {"args": [1], "return": 0},
    {"args": [8], "return": 6},
    {"args": [24], "return": 9},
    {"args": [2], "return": 2},
    {"args": [18], "return": 8},
    {"args": [555], "return": 18},
]


class TestSnakeFill(unittest.TestCase):
    def test_snake_fill(self):
        for test in tests:
            self.assertEqual(snake_fill(*test["args"]), test["return"])
