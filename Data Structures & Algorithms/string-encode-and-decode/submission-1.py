class Solution:

    def encode(self, strs: List[str]) -> str:
        hashCode = "67676767676767"
        ans = "STARTHASH:" + hashCode
        for word in strs:
            newWord = word
            newWord += hashCode
            ans += newWord
        return ans


    def decode(self, s: str) -> List[str]:
        ans = []
        hashCode = s[10:24] #12 long
        idx = 24

        while idx < len(s):
            word = ""
            while s[idx:idx+14] != hashCode:
                word += s[idx]
                idx += 1
            ans.append(word)
            idx = idx+14
        return ans
                    