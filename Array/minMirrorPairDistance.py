from typing import List
from math import inf
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x: int) -> int:
            y = 0
            while x:
                v = x % 10
                y = y * 10 + v
                x //= 10
            return y

        pos = {}
        ans = inf
        for i, x in enumerate(nums):
            print(pos,"Position")
            print(x,"X")
            print (reverse(x),"Reverse X")
            print(i,"I")

            if x in pos:
                ans = min(ans, i - pos[x])
            pos[reverse(x)] = i
            print(ans,"Answer")
        return -1 if ans == inf else ans
    

    #Example usage
solution_instance = Solution()
nums = [123, 321, 456, 654, 789]
result = solution_instance.minMirrorPairDistance(nums)
print(result)