from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k  # ceil division
            return hours <= h

        left, right = 1, max(piles)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if canEat(mid):
                answer = mid
                right = mid - 1   # try smaller speed
            else:
                left = mid + 1     # need faster speed

        return answer
    


#Template for binary search problems
# class Solution:
#     def someFunction(self, input):
#         def condition(mid):
#             # check if mid satisfies the condition
#             return True or False


# left, right = MIN, MAX
# answer = right

# while left <= right:
#     mid = (left + right) // 2
    
#     if can(mid):
#         answer = mid
#         right = mid - 1   # try smaller (minimize answer)
#     else:
#         left = mid + 1

# return answer