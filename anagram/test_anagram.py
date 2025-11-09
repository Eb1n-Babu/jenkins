import unittest
from anagram_ import anagram

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram("listen","silent"), True)

    def test_anagram_fail(self):
        self.assertEqual(anagram("listet","silent"), False)


if __name__ == '__main__':
    unittest.main()