def check_anagram_words(word1, word2):
    try:
        x = sorted(word1.lower())
        y = sorted(word2.lower())
        if x == y:
            return True
        else:
            return False
    except TypeError:
        return False
    except ValueError:
        return False

print(check_anagram_words(word1="hello", word2="world"))
print(check_anagram_words(word1="listen", word2="silent"))