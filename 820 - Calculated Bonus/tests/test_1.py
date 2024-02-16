from main import bonus
import unittest

tests = [
    {"args": [37], "return": 1625},
    {"args": [50], "return": 8200},
    {"args": [15], "return": 0},
]


class TestBonus(unittest.TestCase):
    def test_bonus(self):
        for test in tests:
            self.assertEqual(bonus(*test["args"]), test["return"])
