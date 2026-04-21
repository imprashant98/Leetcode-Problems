from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        parent = list(range(len(source)))
        
        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Union
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # Step 1: Build components
        for a, b in allowedSwaps:
            union(a, b)
        
        # Step 2: Group indices by root
        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)
        
        # Step 3: Calculate Hamming distance
        res = 0
        
        for indices in groups.values():
            source_count = Counter()
            
            # Count values in source
            for i in indices:
                source_count[source[i]] += 1
            
            # Match with target
            for i in indices:
                if source_count[target[i]] > 0:
                    source_count[target[i]] -= 1
                else:
                    res += 1
        
        return res
    

# Example usage
solution = Solution()
source = [1,2,3,4]
target = [2,1,4,5]
allowedSwaps = [[0,1],[2,3]]
print(solution.minimumHammingDistance(source, target, allowedSwaps))