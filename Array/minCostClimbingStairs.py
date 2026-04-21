from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # dp[i-2], dp[i-1]
        prev2, prev1 = cost[0], cost[1]
        
        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr
        
        # You can end from last or second last step
        return min(prev1, prev2)