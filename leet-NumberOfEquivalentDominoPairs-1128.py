# 1128. Number of Equivalent Domino Pairs

# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

# Best description is in the Typescript one 

from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        masterList: List[int] = [0] * 100
        retVal: int = 0
        num1: int = 0
        for domino in dominoes:
            # print(domino)
            # print(domino[0])
            if (domino[0]< domino[1]):
                num1 = domino[0]*10 + domino[1]
            else:
                num1 = domino[1]*10 + domino[0]
            retVal += masterList[num1]
            masterList[num1] += 1
        
        return retVal


thing = Solution()
print(thing.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))