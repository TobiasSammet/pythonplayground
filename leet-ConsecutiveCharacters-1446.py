class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        retVal: int = 0
        currentCount: int = 1
        temp: str = s[0]
        
        for i in range(1, len(s)):
            if s[i] == temp:
                currentCount +=1
            else:
                retVal = max(retVal, currentCount)
                currentCount = 1
                temp= s[i]
        retVal = max(retVal, currentCount)
        return retVal
    
thing = Solution()
print(thing.maxPower('leetcode'))