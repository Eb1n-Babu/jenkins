def check_palindrome(string_word):
    string_word = string_word.replace(' ', '')
    reversed_word = string_word[::-1]
    if string_word == reversed_word and len(string_word) == len(reversed_word):
        return True
    else:
        return False