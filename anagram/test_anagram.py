import unittest
from check_anagram import check_anagram_words


class TestAnagram(unittest.TestCase):
    def test_anagram_words(self):
        self.assertEqual(check_anagram_words(word1="hello", word2="world"), False)
        self.assertEqual(check_anagram_words(word2="listen", word1="silent"), True)

if __name__ == '__main__':
    unittest.main()