from collections import Counter


def characterReplacement(s: str, k: int) -> int:
    ans = 0
    max_count = 0
    count = Counter()
    left = 0

    for right, char in enumerate(s):
        count[char] += 1
        max_count = max(max_count, count[char])

        # If the length of the current substring minus the maximum count exceeds k
        while right - left + 1 - max_count > k:
            count[s[left]] -= 1
            left += 1

        # Update ans with the maximum substring length
        ans = max(ans, right - left + 1)

    return ans


s = "ABAB"
k = 2
print(characterReplacement(s, k))
