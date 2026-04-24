class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count_L = moves.count('L')
        count_R = moves.count('R')
        count_underscore = moves.count('_')
        
        # Option 1: Use all underscores to go right
        max_right = abs((count_R + count_underscore) - count_L)
        
        # Option 2: Use all underscores to go left
        max_left = abs(count_R - (count_L + count_underscore))
        
        return max(max_right, max_left)