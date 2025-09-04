def Palindrome(n):
    n = n.replace(' ', '')
    r = n[::-1]
    if r.upper() == n.upper() and len(r) == len(n):
        return True
    else:
        return False