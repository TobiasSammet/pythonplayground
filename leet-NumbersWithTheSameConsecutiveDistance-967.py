from typing import List

class Solution :
    retVal: List[int]
    def numsSameConsecDiff(self, N: int, K: int) -> List[int] :
        self.retVal = []
        if N == 1: 
            return [0,1,2,3,4,5,6,7,8,9]
        for i in range(1,9,1):
            self.processValue(i, i + K, N , K)
            if K > 0:
                self.processValue(i, i -K, N, K)
        return self.retVal

    def processValue(self, value: int, newValue: int, N: int, K: int):
        if newValue >=0 and newValue <= 9 :
            value = value * 10 + newValue
            if len(str(value)) == N:
                self.retVal.append(value)
            else:
                self.processValue(value, newValue + K, N, K)
                if K > 0 :
                    self.processValue(value, newValue -K, N, K)

thing = Solution()
print(thing.numsSameConsecDiff(3,7))