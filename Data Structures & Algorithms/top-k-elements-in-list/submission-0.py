from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = defaultdict(int)
        for num in nums:
            values[num] += 1
        
        dictList = list(values.items())
        dictList.sort(key = lambda x: x[1], reverse = True)
        ans = dictList[:k]

        return [x[0] for x in ans]