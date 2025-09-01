class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        currentPos: int = 0
        characterToFind: str = s[currentPos]
        for char in t:
            if char == characterToFind:
                if currentPos == len(s) - 1:
                    return True
                currentPos += 1
                characterToFind = s[currentPos]
        return False
    

thingy = Solution()


print(thingy.isSubsequence('abc', 'ahbgdc')) # True
print(thingy.isSubsequence('axc', 'ahbgdc')) # False
print(thingy.isSubsequence("abc", "abc")) # True
# print(thingy.isSubsequence())