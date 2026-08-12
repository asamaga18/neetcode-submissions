class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix array
        prefix = []
        total = 1
        for idx, num in enumerate(nums):
            prefix.append(total)
            total = total * num
        
        ans = []
        sufTotal = 1
        for idx, num in reversed(list(enumerate(nums))):
            ans.append(sufTotal * prefix[idx])
            sufTotal = sufTotal * num
        return list(reversed(ans))