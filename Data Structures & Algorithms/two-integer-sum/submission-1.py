class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for idx, num in enumerate(nums):
            goal = target - num
            if goal in seen:
                if idx > seen[goal]:
                    return [seen[goal], idx]
                else:
                    return [idx, seen[goal]]
            else:
                seen[num] = idx