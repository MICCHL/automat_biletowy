import unittest

import interface


class TestInterface(unittest.TestCase):

    def setUp(self):
        self.maschine = interface.Maschine()

    def test_throwing(self):
        self.assertEqual(self.maschine.throw_coins(1.0), 1.0)


if __name__ == '__main__':
    unittest.main()