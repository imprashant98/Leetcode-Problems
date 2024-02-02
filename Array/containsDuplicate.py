from typing import List


class Solution:
    def containsDupliicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        while (i < len(nums)-1):
            currNum = nums[i]
            nextNum = nums[i+1]
            if currNum == nextNum:
                return True

            i += 1
            return False


solution_ins = Solution()
nums = [1, 2, 3, 1]
result = solution_ins.containsDupliicate(nums)
print(result)
