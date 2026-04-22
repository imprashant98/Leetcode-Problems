from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        
        for query in queries:
            for dict_word in dictionary:
                differences = 0
                for i in range(len(query)):
                    if query[i] != dict_word[i]:
                        differences += 1
                        if differences > 2:
                            break
                
                if differences <= 2:
                    result.append(query)
                    break
        
        return result