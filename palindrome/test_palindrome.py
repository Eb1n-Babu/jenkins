import unittest
from palindrome import Palindrome


class test_palindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(Palindrome('hello'), False)
        self.assertTrue(Palindrome('malayalam'))
        self.assertFalse(Palindrome('hello'))

if __name__ == '__main__':
    unittest.main()