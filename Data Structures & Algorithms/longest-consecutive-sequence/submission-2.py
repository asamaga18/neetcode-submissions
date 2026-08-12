class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = list(set(nums))
        newNums.sort()
        
        if not nums:
            return 0
        
        print(newNums)
        ans = 1
        counter = 1
        for idx, num in enumerate(newNums[1:]):
            idx = idx+1
            
            if num == newNums[idx-1]+1:
                counter += 1
            else:
                ans = max(ans, counter)
                counter = 1
        
        return max(ans, counter)