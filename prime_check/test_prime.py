import unittest
from prime import *


class test_prime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(find_prime(2))
        self.assertTrue(find_prime(3))
        self.assertFalse(find_prime(4))
        self.assertTrue(find_prime(5))
        self.assertFalse(find_prime(6))
        self.assertTrue(find_prime(7))
        self.assertFalse(find_prime(8))
        self.assertFalse(find_prime(9))
        self.assertFalse(find_prime(10))

if __name__ == '__main__':
    unittest.main()
