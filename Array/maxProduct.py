# from typing import List


# class Solution:
#     def maxProdcut(self, nums: List[int]) -> int:
#         n = len(nums)
#         a = b = 1
#         ans = float('-inf')

#         for i in range(1, n+1):
#             tmp = a
#             a = max(a*nums[i-1], b*nums[i-1], nums[i-1])
#             b = max(tmp * nums[i-1], b*nums[i-1], nums[i-1])
#             ans = max(ans, a)
#         return ans


# nums = [2, 3, -2, 4]
# # nums = [-2, 0, -1]
# print(Solution().maxProdcut(nums))

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        a = b = 1
        ans = float('-inf')

        for i in range(n):
            tmp = a
            a = max(a * nums[i], b * nums[i], nums[i])
            b = min(tmp * nums[i], b * nums[i], nums[i])
            ans = max(ans, a)

        return ans


nums = [2, 3, -2, 4]
# nums = [-2, 0, -1]
print(Solution().maxProduct(nums))
