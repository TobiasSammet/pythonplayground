class Solution :
    def addDigits(self, num: int) -> int :
        tempSum: int = num
        while tempSum >= 10 :
            theNewNumber: int = tempSum
            tempSum = 0
            while theNewNumber > 0:
                tempSum += theNewNumber % 10
                theNewNumber = theNewNumber // 10
        return tempSum

thing = Solution()
print(thing.addDigits(38)) # 2
print(thing.addDigits(10)) # 1