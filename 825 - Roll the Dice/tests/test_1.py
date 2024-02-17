from main import dice
import unittest

tests = [
    {"args": [3], "return": "O--/-O-/--O"},
    {
        "args": [63],
        "return": "O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O, O--/-O-/--O",
    },
    {"args": [11], "return": "O-O/O-O/O-O, O-O/-O-/O-O"},
    {"args": [18], "return": "O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O"},
    {"args": [6], "return": "O-O/O-O/O-O"},
    {"args": [9], "return": "O-O/O-O/O-O, O--/-O-/--O"},
    {"args": [1], "return": "---/-O-/---"},
    {"args": [20], "return": "O-O/O-O/O-O, O-O/O-O/O-O, O-O/O-O/O-O, O--/---/--O"},
    {"args": [8], "return": "O-O/O-O/O-O, O--/---/--O"},
]


class TestDice(unittest.TestCase):
    def test_dice(self):
        for test in tests:
            self.assertEqual(dice(*test["args"]), test["return"])
