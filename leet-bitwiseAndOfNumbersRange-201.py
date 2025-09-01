class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        if n - m > 100:
            return 0
        retVal:int = m
        for i in range(m+1, n + 1, 1) :
            retVal = retVal & i
            if retVal == 0 :
                return 0

        return retVal

thing = Solution()
# print(thing.rangeBitwiseAnd(5,7))
# print(thing.rangeBitwiseAnd(5,7))
print(thing.rangeBitwiseAnd(2147483646, 2147483647))
