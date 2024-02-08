def longest_palindromic_substring(s):
    n = len(s)
    # Initialize a table to store whether substring i to j is a palindrome
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for substrings of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length

    return s[start:start + max_length]


# Test the function with the given input
S = "aaaabbaa"
output = longest_palindromic_substring(S)
print("Output:", output)
