def countSubstrings(s: str) -> int:
    def extendPalindrimes(l: int, r: int) -> int:
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
    ans = 0

    for i in range(len(s)):
        ans += extendPalindrimes(i, i)
        ans += extendPalindrimes(i, i+1)
    return ans


s = "abc"
print(countSubstrings(s))
