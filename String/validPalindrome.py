def isPalindrome(s: str) -> bool:
    s = ''.join([c for c in s.lower() if c.isalnum()])
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True


s = "ramar"
print(isPalindrome(s))
