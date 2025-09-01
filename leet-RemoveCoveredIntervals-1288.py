from typing import List

class Solution :
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        length: int = len(intervals)
        retVal: int = length
        for i in range(length):
            for j in range(length):
                if i != j :
                    if (intervals[j][0] <= intervals[i][0]) and (intervals[i][1] <= intervals[j][1]) :
                        retVal -=1
                        break
        return retVal

thing = Solution()
intervals: List[List[int]] = [[1,2],[1,4],[3,4]]
print(thing.removeCoveredIntervals(intervals))