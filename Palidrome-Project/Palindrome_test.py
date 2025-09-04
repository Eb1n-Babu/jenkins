import unittest
from Palindrome import check_palindrome


class testPalindrome(unittest.TestCase):
    def testPalindrome(self):
        self.assertEqual(check_palindrome("abba"), True)
        self.assertEqual(check_palindrome("ab    ba"), True)
        self.assertEqual(check_palindrome("abSabaDEFDFE"), False)
        self.assertEqual(check_palindrome("1234567"), False)

if __name__ == '__main__':
    unittest.main()
