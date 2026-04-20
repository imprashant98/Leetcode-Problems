
from typing import List
import bisect
import math 

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []
        
        for s in spells:
            # minimum potion needed
            # target = (success + s -1) // s  # equivalent to math.ceil(success / s)
            target = math.ceil(success / s)  # ceil division
            print(f"Spell: {s}, Target Potion Strength: {target}")
            
            # find first index where potion >= target
            idx = bisect.bisect_left(potions, target) # returns the leftmost index to insert target
            print(f"First index in potions where potion >= target: {idx}")
            
            result.append(n - idx)
            print(f"Successful pairs for spell {s}: {n - idx}")
        
        return result

# example usage
solution = Solution()
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(solution.successfulPairs(spells, potions, success))  # Output: [4, 0, 3]