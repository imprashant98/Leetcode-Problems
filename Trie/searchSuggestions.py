from typing import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        
        for ch in searchWord:
            prefix += ch
            
            # Find the first index where prefix can be inserted
            i = bisect.bisect_left(products, prefix)
            
            suggestions = []
            # Check next 3 products
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
            
            res.append(suggestions)
        
        return res