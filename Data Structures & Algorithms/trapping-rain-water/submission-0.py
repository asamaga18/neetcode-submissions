class Solution:
    def trap(self, height: List[int]) -> int:
        # watched how neetcode did it, going to try and translate it to code
        maxLeft = 0
        maxRight = 0

        left = 0
        right = len(height) - 1
        ans = 0
        while left <= right:
            if maxLeft <=  maxRight:
                ans += max(0, maxLeft - height[left])
                maxLeft = max(maxLeft, height[left])
                left += 1

            else:
                ans += max(0, maxRight - height[right])
                maxRight = max(maxRight, height[right])
                right -= 1
        return ans