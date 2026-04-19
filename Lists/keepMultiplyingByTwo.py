from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        while original in num_set:
            original *= 2
        
        return original

# Example usage
solution_instance = Solution()
nums = [5, 3, 6, 1, 12]
original = 3
result = solution_instance.findFinalValue(nums, original)
print(result)