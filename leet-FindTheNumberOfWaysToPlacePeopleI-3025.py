from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        length: int = len(points)
        if length <= 1:
            return 0
        retVal: int = 0
        for i in range(0, length):
            for j in range(0, length):
                if i != j:
                    if points[i][0] >= points[j][0] and points[i][1] <= points[j][1]:
                        blocked: bool = False
                        # let's check if there are any points in the way of our rectange
                        for k in range(0, length):
                            if k != i and k != j:
                                if points[i][0] >= points[k][0] and points[k][0] >= points[j][0] and points[i][1] <= points[k][1] and points[k][1] <= points[j][1]:
                                    blocked = True
                                    break
                        if blocked == False:
                            retVal += 1
        return retVal


def main():
    thingy = Solution()
    print(thingy.numberOfPairs([[1,1],[2,2],[3,3]])) # 0
    print(thingy.numberOfPairs([[6,2],[4,4],[2,6]])) # 2
    print(thingy.numberOfPairs([[3,1],[1,3],[1,1]])) # 2



if __name__ == "__main__":
    main()