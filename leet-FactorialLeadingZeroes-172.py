class Solution:
    def trailingZeroes(self, n: int) -> int:
        retVal: int = 1
        if n < 5 :
            return 0
        if n < 10 : 
            return 1
        for i in range(10, n + 1) :
            if i % 5 == 0 :
                retVal += 1
                temp = i / 5
                while temp % 5 == 0 :
                    retVal += 1
                    temp = temp //  5
        return retVal

thing = Solution()
print(thing.trailingZeroes(30))