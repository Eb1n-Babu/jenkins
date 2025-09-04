import unittest
from prime_check.prime import prime_check


class test_prime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(prime_check(2))
        self.assertTrue(prime_check(3))
        self.assertFalse(prime_check(4))
        self.assertTrue(prime_check(5))
        self.assertFalse(prime_check(6))
        self.assertTrue(prime_check(7))
        self.assertFalse(prime_check(8))
        self.assertFalse(prime_check(9))
        self.assertFalse(prime_check(10))

if __name__ == '__main__':
    unittest.main()
