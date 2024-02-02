from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        return nums[l]


# nums = [3, 4, 5, 1, 2]
nums = [1, 2, 3, 4, 5]
print(Solution().findMin(nums))
