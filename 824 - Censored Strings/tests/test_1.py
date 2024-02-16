from main import unsensor
import unittest

tests = [
    {
        "args": ["*l*ph*nt", "Eea"],
        "return": "Elephant"
    },
    {
        "args": ["abcd", ""],
        "return": "abcd"
    },
    {
        "args": ["Ch**s*, Gr*mm*t -- ch**s*", "eeeoieee"],
        "return": "Cheese, Grommit -- cheese"
    },
    {
        "args": ["*PP*RC*S*", "UEAE"],
        "return": "UPPERCASE"
    },
    {
        "args": ["Wh*r* d*d my v*w*ls g*?", "eeioeo"],
        "return": "Where did my vowels go?"
    }
]

class TestUnsensor(unittest.TestCase):
    def test_unsensor(self):
        for test in tests:
            self.assertEqual(unsensor(*test["args"]), test["return"])