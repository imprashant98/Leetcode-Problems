from typing import List
import collections


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dict_anagrams = collections.defaultdict(list)

    for string in strs:
        key = ''.join(sorted(string))
        dict_anagrams[key].append(string)

    return list(dict_anagrams.values())


# Example usage
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(input_strings)
print(result)
