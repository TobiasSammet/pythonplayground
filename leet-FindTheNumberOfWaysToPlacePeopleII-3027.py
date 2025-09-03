from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        length: int  = len(points)
        if length <= 1: 
            return 0
        retVal: int = 0
        points.sort(key=lambda x: (x[0], -x[1]))
        
        for i in range(0, length-1):
            topLeft = points[i]
            xValues = [topLeft[0]-1, float('inf')]
            yValues = [float('-inf'), topLeft[1] + 1]
            for j in range(i+1, length):
                bottomRight = points[j]
                if bottomRight[0] > xValues[0] and \
                    bottomRight[1] > yValues[0] and \
                    bottomRight[1] < yValues[1]:
                    retVal += 1
                    xValues[0] = bottomRight[0]
                    yValues[0] = bottomRight[1]
        return retVal


def main():
    thingy = Solution()
    print(thingy.numberOfPairs([[1,1],[2,2],[3,3]])) # 0
    print(thingy.numberOfPairs([[6,2],[4,4],[2,6]])) # 2
    print(thingy.numberOfPairs([[3,1],[1,3],[1,1]])) # 2


if __name__ == "__main__":
    main()