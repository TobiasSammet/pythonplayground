# when you only have a min heap you negate the value you want to max

from typing import List
from heapq import heappush, heappop, heapify

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        theHeap = []
        length: int = len(classes)
        if length == 0: 
            return 0
        for i in range(0, length):
            currentRatio = classes[i][0] / classes[i][1]
            newRatio = (classes[i][0] + 1) / (classes[i][1] + 1)
            heappush(theHeap, (-1 * (newRatio - currentRatio), classes[i][0], classes[i][1]))

        for i in range(0, extraStudents):
            ratio, passing, total = heappop(theHeap)
            passing += 1
            total += 1
            currentRatio = passing / total
            newRatio = (passing + 1) / (total + 1)
            heappush(theHeap, (-1 * (newRatio - currentRatio), passing, total))
        retVal: int = 0

        while len(theHeap) > 0:
            ratio, passing, total = heappop(theHeap)
            retVal += (passing/total)

        return retVal / length

def main():
    thingy = Solution()

    # 0.78333
    print(thingy.maxAverageRatio([[1,2],[3,5],[2,2]], 2))

    # 0.53485
    print(thingy.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))

if __name__ == "__main__":
    main()