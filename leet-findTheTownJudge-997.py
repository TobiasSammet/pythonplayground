from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if (N == 1) and (len(trust) == 0):
            return 1
        if (N <= 1) and (len(trust) == 0):
            return -1
        trustCount: List[int] = [0] * (N+1)
        for item in trust:
            trustCount[item[1]] += 1
            trustCount[item[0]] -= 1
        for i in range(1, N + 1):
            if trustCount[i] == N-1:
                return i

        return -1

thing = Solution()
trust: List[List[int]] = [[1, 3],[1,4],[2,3],[2,4],[4,3]]

print(thing.findJudge(4, trust))