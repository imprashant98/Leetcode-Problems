from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        nums_len = len(nums)
        for curr_idx in range(nums_len):
            curr_num = nums[curr_idx]  # Use square brackets for indexing
            remaining = target - curr_num
            if remaining in visited:
                visited_idx = visited[remaining]
                return [visited_idx, curr_idx]
            else:
                visited[curr_num] = curr_idx


# Create an instance of the Solution class
solution_instance = Solution()

# Call the two_sum method on the instance
nums = [2, 7, 11, 15]
target = 9
result = solution_instance.two_sum(nums, target)

# Print the result
print(result)
