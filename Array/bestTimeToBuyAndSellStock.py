from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_ptr, profit = 0, 0
        for right_ptr in range(1, len(prices)):
            if prices[left_ptr] < prices[right_ptr]:
                profit = max(profit, prices[right_ptr] - prices[left_ptr])
            else:
                left_ptr = right_ptr

        return profit


# Create an instance of the Solution class
solution_instance = Solution()

prices = [7, 1, 5, 3, 6, 4]
result = solution_instance.maxProfit(prices)
print(result)
