from typing import List


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     max_sum_ending_idx = max_sum = nums[0]
    #     for i in range(1, n):
    #         max_sum_ending_idx = max(max_sum_ending_idx+nums[i], nums[i])
    #         max_sum = max(max_sum_ending_idx, max_sum)
    #     return (max_sum)
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
