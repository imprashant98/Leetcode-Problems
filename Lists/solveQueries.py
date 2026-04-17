from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Map each value to sorted indices
        value_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            value_to_indices[val].append(i)
        
        n = len(nums)
        result = []
        
        for q in queries:
            val = nums[q]
            indices = value_to_indices[val]
            
            if len(indices) == 1:
                result.append(-1)
                continue
            
            # Find position of q in indices list using binary search
            pos = bisect.bisect_left(indices, q)
            m = len(indices)
            
            # Check left neighbor (wrap around)
            left_idx = indices[(pos - 1) % m]
            clockwise_dist = (left_idx - q) % n
            counterclockwise_dist = (q - left_idx) % n
            min_distance = min(clockwise_dist, counterclockwise_dist)
            
            # Check right neighbor (wrap around)
            right_idx = indices[(pos + 1) % m]
            clockwise_dist = (right_idx - q) % n
            counterclockwise_dist = (q - right_idx) % n
            min_distance = min(min_distance, clockwise_dist, counterclockwise_dist)
            
            result.append(min_distance)
        
        return result