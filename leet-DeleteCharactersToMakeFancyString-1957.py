class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        retVal: str = s[0:2]
        oldestChar: str = s[0]
        lastChar: str = s[1]
        for i in range(2, len(s)):
            if (oldestChar == lastChar) and (lastChar == s[i]):
                pass
            else:
                oldestChar = lastChar
                lastChar = s[i]
                retVal += lastChar 

        return retVal

thingy = Solution()

print(thingy.makeFancyString('leeetcode')); # "leetcode"
print(thingy.makeFancyString('aaabaaaa')); # "aabaa"
print(thingy.makeFancyString('aab')); # "aab"