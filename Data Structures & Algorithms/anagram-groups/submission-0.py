from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = "".join(sorted(word))
            groups[count].append(word)
        
        return list(groups.values())
