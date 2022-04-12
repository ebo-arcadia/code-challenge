import unittest
# from die import Die
class Die:
    def __init__(self, sides=6):
        self.sides = sides


class TestDieFunction(unittest.TestCase):

    def setUp(self):
        self.die1 = Die()
        self.die2 = Die(8)
        self.die3 = Die(10)

    def test_init(self):
        self.assertEqual(self.die1.sides, 6)
        self.assertEqual(self.die2.sides, 8)
        self.assertEqual(self.die3.sides, 10)


if __name__ == '__main__':
    unittest.main()
