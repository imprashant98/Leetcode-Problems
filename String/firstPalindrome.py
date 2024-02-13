from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


# Create an instance of the Solution class
solution_instance = Solution()

words = ["abc", "car", "ada", "racecar", "cool"]
output = solution_instance.firstPalindrome(words)
print(output)  # Output: "ada"
