from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums) # O(n) time to create set and O(n) space
        longest_subsequence= 0
        # print(f"Unique numbers in the set: {num_set}")

        for num in num_set:
            # Check if this is the start of a sequence
            # (no smaller consecutive number exists)
            if num - 1 not in num_set:
                current_num = num
                current_subsequence = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_subsequence += 1 
                
                longest_subsequence = max(longest_subsequence, current_subsequence)
        
        return longest_subsequence
    
# Example usage:
nums = [100, 4, 200, 1, 3, 2]
solution = Solution()
result = solution.longestConsecutive(nums)
print(f"Longest consecutive subsequence length: {result}")