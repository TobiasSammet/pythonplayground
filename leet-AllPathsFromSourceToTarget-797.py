from typing import List


class Solution:
    theGraph: List[List[int]]
    safePath: List[List[int]]
    endValue: int

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.endValue = len(graph) -1
        self.theGraph = graph
        self.safePath = []
        if len(graph) == 0:
            return self.safePath

        for i in self.theGraph[0]:
            currentPath: List[int] = [0]
            self.processValue(i, currentPath)
        return self.safePath

    def processValue(self, index: int, currentPath: List[int]) -> None:
        currentPath.append(index)
        if index == self.endValue :
            self.safePath.append(currentPath)
            return
        
        for i in self.theGraph[index]:
            if i not in currentPath:
                temp: List[int] = currentPath.copy()
                self.processValue(i, temp)

thing = Solution()
graph: List[List[int]] = [[1,2],[3],[3],[]]
print(thing.allPathsSourceTarget(graph))