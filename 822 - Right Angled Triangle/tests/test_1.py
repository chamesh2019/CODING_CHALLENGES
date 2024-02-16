from main import right_triangle
import unittest

tests = [
        {"args": [915, 1748, 1973], "return": True},
        {"args": [0, 4, 4], "return": False},
        {"args": [70, 130, 110], "return": False},
        {"args": [140, 170, 220], "return": False},
        {"args": [60, 60, 60], "return": False},
        {"args": [145, 105, 100], "return": True},
        {"args": [3, 4, 5], "return": True},
        {"args": [115, 277, 252], "return": True},
        {"args": [-3, 4, 5], "return": False},
]


class TestRightTriangle(unittest.TestCase):
    def test_right_triangle(self):
        for test in tests:
            self.assertEqual(right_triangle(*test["args"]), test["return"])
