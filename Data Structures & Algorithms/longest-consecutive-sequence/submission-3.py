class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        for num in numSet:
            prev = num - 1
            if prev in numSet:
                continue
            else:
                #this is the left most
                counter = 1
                start = num
                while True:
                    if start+1 in numSet:
                        counter += 1
                        start += 1
                    else:
                        break
                ans = max(ans, counter)
        return ans