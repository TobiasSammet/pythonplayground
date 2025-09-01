from typing import List

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True
        numLength = len(str(n))
        numCount: List[int] = self.getFrequencyCount(n)
        powersOfTwo: List[int] = []
        i: int = 2

        while len(str(i)) <= numLength:
            if len(str(i)) == numLength:
                powersOfTwo.append(i)
            i = i * 2

        for item in powersOfTwo:
            freqCount: List[int] = self.getFrequencyCount(item)
            tempRet: bool = True
            for i in range(0,10):
                if numCount[i] != freqCount[i]:
                    tempRet = False
                    break
            if tempRet == True: 
                return True
        

        return False
    
    def getFrequencyCount(self, n: int) -> List[int]:
        numCount: List[int] = [0] * 10
        while n > 0:
            numCount[n % 10] += 1
            n = n // 10
        return numCount
    

thingy = Solution()

print(thingy.reorderedPowerOf2(1))
# print(thingy.reorderedPowerOf2(10))
print(thingy.reorderedPowerOf2(46))
print(thingy.reorderedPowerOf2(8388608))