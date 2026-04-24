
from collections import defaultdict
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        value_to_indices = defaultdict(list)
        for index, num in enumerate(nums):
            value_to_indices[num].append(index)
        
        result = [0] * len(nums)
        
        for indices in value_to_indices.values():
            if len(indices) > 1:
                group_size = len(indices)
                first_index = indices[0]
                result[first_index] = sum(indices) - group_size * first_index
                
                left_count, right_count = 0, group_size - 2
                current_index = first_index
                
                for next_index in indices[1:]:
                    result[next_index] = result[current_index] + (left_count - right_count) * (next_index - current_index)
                    left_count += 1
                    right_count -= 1
                    current_index = next_index
        
        return result