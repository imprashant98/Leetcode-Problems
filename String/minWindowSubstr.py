import collections


def minWindowSubstring(s: str, t: str) -> str:
    count = collections.Counter(t)
    required = len(t)
    bestLeft = -1
    minLen = len(s) + 1
    l = 0

    for r, c in enumerate(s):
        count[c] -= 1
        if count[c] >= 0:
            required -= 1

        while required == 0:
            if r - l + 1 < minLen:
                bestLeft = l
                minLen = r - l + 1

            if count[s[l]] >= 0:
                required += 1
            count[s[l]] += 1
            l += 1

    return '' if bestLeft == -1 else s[bestLeft:bestLeft + minLen]


# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(minWindowSubstring(s, t))
