from typing import List

class Solution:
    combos: List[List[int]] 

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.combos = []
        if k == 0 or n == 0:
            return self.combos
        
        for i in range(1,10):
            if i <= n:
                tempList: List[int] = []
                self.processNumber(k,n,i,tempList)

        return self.combos

    def processNumber(self, count: int, destination: int, newNumber: int, currentList: List[int]):
        if destination - newNumber < 0:
            return
        if newNumber in currentList:
            return
        if len(currentList) == count:
            return
        newList: List[int] = currentList.copy()
        newList.append(newNumber)
        destination -= newNumber
        if destination == 0 and len(newList) == count:
            if not self.alreadyExists(newList) :
                self.combos.append(newList)
            return
        for i in range(1,10):
            self.processNumber(count, destination, i, newList)





    def alreadyExists(self, newList: List[int]) -> bool:
        retVal: bool = True
        if len(self.combos) == 0:
            return False
        for tempList in self.combos:
            retVal = True
            for value in tempList:
                if not value in newList:
                    retVal = False
                    break
                    
            if retVal == True :
                return True

        return False


thing = Solution()
print(thing.combinationSum3(3,9))