from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end first, then by start
        intervals.sort(key=lambda x: (x[1], -x[0])) # Sort by end first, then by start in descending order to ensure we pick the largest possible points
        
        # a = second last picked, b = last picked
        a = b = -1
        res = 0
        
        for l, r in intervals:
            if l <= a:
                # already has at least 2 points
                continue
            elif l <= b:
                # has exactly 1 point, add one more
                res += 1
                a = b
                b = r
            else:
                # has 0 points, add two
                res += 2
                a = r - 1
                b = r
        
        return res