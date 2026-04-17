from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        
        def dfs():
            total = 0
            for char in freq:
                if freq[char] > 0:
                    freq[char] -= 1
                    total += 1 + dfs() 
                    freq[char] += 1
            return total
        
        return dfs()