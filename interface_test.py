import unittest

import interface


class TestInterface(unittest.TestCase):

    def setUp(self):
        self.Maschine = interface.Maschine()

    def test_throwing(self):
        result = self.Maschine.sum_coins(1.0)
        self.assertEqual(result, 1.0)


if __name__ == '__main__':
    unittest.main()