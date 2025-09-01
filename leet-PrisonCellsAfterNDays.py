from typing import List

def printList(cells: List[int]) -> str :
    retVal: str = ""
    for value in cells:
        retVal += " " + str(value)
    return retVal.strip()

class Solution :
    VACANT: int = 0
    OCCUPIED: int = 1
    def prisonAfterNDays(self,cells: List[int], N: int) -> List[int]:
        if N==0:
            return cells
        N = N %14
        if N == 0 :
            N = 14
        listLength: int = len(cells)
        currentGen: List[int]
        currentGen = cells.copy()
        for x in range(N):
            nextGen: List[int] = [self.VACANT] * listLength
            for i in range(1, listLength-1):
                if currentGen[i-1] == currentGen[i+1]:
                    nextGen[i] = self.OCCUPIED
            currentGen = nextGen.copy()

        return currentGen

    def helloWorld(self, s: str) -> str :
        return 'Hello ' + s


thing = Solution()
cells: List[int] = [0,1,0,1,1,0,0,1]

# print(printList(thing.prisonAfterNDays(cells, 1)))
for i in range(1,8) :
    print(i)
    print(printList(thing.prisonAfterNDays(cells, i)))

