class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        retVal: int = 0
        haveMiddle: bool = False
        newString: str = ''.join(sorted(s)) 
        currentChar: str = newString[0]
        currentCount: int = 1
        for i in range(1, len(newString)+ 1) :
            if i == len(newString) or newString[i] != currentChar :
                if not haveMiddle and currentCount % 2 == 1 :
                    haveMiddle = True
                    retVal += 1
                retVal += (currentCount // 2) * 2
                if i == len(newString):
                    break
                currentChar = newString[i]
                currentCount = 1
            else :
                currentCount +=1
        return retVal

thing = Solution()
# print(thing.longestPalindrome('zZZabcccccddC'))
print(thing.longestPalindrome('abccccdd'))
