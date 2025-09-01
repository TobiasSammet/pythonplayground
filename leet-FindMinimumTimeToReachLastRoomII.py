from typing import List
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        rows = len(moveTime)
        cols = len(moveTime[0])
        INF = float('inf')
        dp = [[INF]*cols]*rows
        nextMove = [(0, 0 , 0)]
        print(moveTime)
        moveTime[0][0] = 0
        print(dp)
        print(moveTime)
        return -1
    


thing = Solution()

print(thing.minTimeToReach( [[0,0,0,0],[0,0,0,0]]))