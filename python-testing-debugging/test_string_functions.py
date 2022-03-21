import unittest
from string_functions import *


class TestStringFunctions(unittest.TestCase):

    def test_prepend(self):
        self.assertEqual(prepend('love', 'wisdom'), 'wisdomlove')

    def test_append(self):
        self.assertEqual(append('love', 'wisdom'), 'lovewisdom')

    def test_insert(self):
        self.assertEqual(insert('sation', 'tisfac', 2), 'satisfaction')


if __name__ == '__main__':
    unittest.main()
