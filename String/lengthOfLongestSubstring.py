def lengthOfLongestSubstring(s: str) -> int:
    seen_chars = {}
    max_len = 0
    start = 0
    for end in range(len(s)):
        if s[end] in seen_chars and seen_chars[s[end]] >= start:
            start = seen_chars[s[end]] + 1
        seen_chars[s[end]] = end
        max_len = max(max_len, end - start + 1)
    return max_len


# Call the function directly
s = "abcabcbb"
print(lengthOfLongestSubstring(s))
