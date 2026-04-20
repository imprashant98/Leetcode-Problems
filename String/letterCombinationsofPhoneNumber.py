from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            # base case: full combination formed
            if index == len(digits):
                result.append("".join(path)) # add the combination to the result which is a list of characters, we join them to form a string
                return

            for ch in mapping[digits[index]]:   # iterate through the possible characters for the current digit
                path.append(ch) # choose the character
                backtrack(index + 1, path) # move to the next digit
                path.pop()  # undo (backtrack) the choice for the next iteration

        backtrack(0, [])
        return result