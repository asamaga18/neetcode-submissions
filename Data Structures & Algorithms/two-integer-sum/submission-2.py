class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for idx, num in enumerate(nums):
            goal = target - num
            if goal in seen:   
                return [seen[goal], idx]
                
            else:
                seen[num] = idx