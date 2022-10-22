import unittest
from laba import labwr

class TestNumber(unittest.TestCase):
    def test_something(self):
        self.assertEqual(labwr("привет, друзья"),"Привет, друзья!")  # add assertion here


if __name__ == '__main__':
    unittest.main()
