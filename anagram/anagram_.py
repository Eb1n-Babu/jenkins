def anagram(word_1,word_2):
    w1 = sorted(word_1.lower())
    w2 = sorted(word_2.lower())
    if len(w1) == len(w2):
        for i in range (len(w1)):
            if w1[i] == w2[i]:
                continue
            else:
                return False
        return True
    else:
        return False





