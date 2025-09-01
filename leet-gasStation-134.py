from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) != len(cost):
            return -1
        if min(gas) < 0 or min(cost) < 0 :
            return -1
        retVal: int = -1
        length: int = len(gas)
        if length == 1:
            if cost[0] > gas[0]:
                return -1
            else:
                return 0
        for i in range(0,length):
            if  gas[i] > cost[i]:
                retVal = self.StartHere(i, gas, cost)
            if retVal > -1:
                break
        
        return retVal
        
    def StartHere(self, startingIndex: int, gas: List[int], cost: List[int]) -> int:
        retVal: int =  -1
        length: int = len(gas)
        currentIndex: int = startingIndex
        currentGas: int = gas[startingIndex]

        while currentGas >= cost[currentIndex]:
            currentGas -= cost[currentIndex]
            currentIndex = (currentIndex + 1) % length
            currentGas += gas[currentIndex]
            if currentIndex == startingIndex:
                retVal = startingIndex
                break

        return retVal

thing = Solution()
print(thing.canCompleteCircuit([2,3,4], [3,4,3]))