class Solution:
    def isPalindrome(self, s: str) -> bool:
        #process the string
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        print(newStr)

        left = 0
        right = len(newStr) - 1

        while left <= right:
            if newStr[left] != newStr[right]:
                return False
            right -= 1
            left += 1
        return True