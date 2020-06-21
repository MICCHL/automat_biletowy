import unittest

import interface

class TestInterface(unittest.TestCase):
    def test_throwing(self):
        result = interface.Maschine.sum_coins(1.0)
        self.assertEqual(result, 1.0)

    def test_throwing1(self):
        result = interface.Maschine.throw_coins(1.0)
        self.assertEqual(result, 1.0)


if __name__ == '__main__':
    unittest.main()