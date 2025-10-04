from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currentVal: int = len(strs[0])
        for i in range(1, len(strs)):
            fullMatch: bool = True
            for j in range(0, min(currentVal, len(strs[i]))):
                if strs[i-1][j] != strs[i][j]:
                    fullMatch = False
                    currentVal = j
                    break
            if fullMatch == True:
                currentVal = min(currentVal, len(strs[i]))
        return strs[0][0:currentVal]

    


thingy = Solution()

print(thingy.longestCommonPrefix(['flower', 'flow', 'flight'])) # 'fl'
print(thingy.longestCommonPrefix(['dog', 'racecar', 'car'])) #  ''
print(thingy.longestCommonPrefix(["ab", "a"])) # "a"
# print(thingy.longestCommonPrefix()) #