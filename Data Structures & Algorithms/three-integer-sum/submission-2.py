from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ansDict = defaultdict(set)
        for idx, num in enumerate(nums):
            target = -num

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                sumNum = nums[left] + nums[right]

                if sumNum == target:
                    ansDict[0].add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sumNum > target:
                    right -= 1
                    
                else:
                    left += 1
        ans = []
        for tup in ansDict[0]:
            ans.append(list(tup))
        return ans