class Solution:
    def reverseBits(self, n: int) -> int:
        tempVal = bin(n)[2:].zfill(32)

        reversed: str = ''
        for i in range(0,32):
            reversed = tempVal[i] + reversed

        retVal: int = 0
        for i in range(0,32):
            temp = reversed[i]
            if temp == '1':
                retVal = 2 * retVal + 1
            else:
                retVal = 2 * retVal
        return retVal
    

thingy = Solution()

print(thingy.reverseBits(43261596)) # 964176192
print(thingy.reverseBits(2147483644)) # 1073741822
# print(thingy.reverseBits())