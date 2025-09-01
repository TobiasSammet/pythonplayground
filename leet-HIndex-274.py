from typing import List

class Solution :
    def hIndex(self, citations: List[int]) -> int :
        if len(citations) == 0:
            return 0
        if len(citations) == 1:
            return min(1, citations[0])
        n: int = len(citations)
        bucket: List[int] = [0] * (n + 1)
        
        for i in range(n):
            if citations[i] > n:
                bucket[n] += 1
            else:
                bucket[citations[i]] += 1
        countSum: int = 0
        for i in range(n, 0, -1):
            countSum += bucket[i]
            if countSum >= i:
                return i
        return 0

thing = Solution()
citations: List[int] = [3,0,6,1,5]
print(thing.hIndex(citations))