from typing import List
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        left = 0
        while colors[left] == colors[-1]: # Move left pointer until we find a different color from the last house
            left += 1
        
        right = n - 1
        while colors[right] == colors[0]: # Move right pointer until we find a different color from the first house
            right -= 1
        
        return max(n - 1 - left, right)
    
#example usage
solution = Solution()
colors = [4,4,4,11,4,4,11,4,4,4,4,4]
print(solution.maxDistance(colors))  # Output: 8