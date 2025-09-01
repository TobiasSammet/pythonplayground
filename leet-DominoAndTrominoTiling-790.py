# 790. Domino and Tromino Tiling

# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, 
# return it modulo 10^9 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

# This breaks into this formula (don't ask me how though)
# dp[i] = 2 * dp[i - 1] + dp[i - 3]
from typing import List

class Solution:
    
    def numTilings(self, n: int) -> int:
        mod = (10**9+7)
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        if (n == 3):
            return 5
        dpList: List[int] = [0] * (n+1)
        dpList[1] = 1
        dpList[2] = 2
        dpList[3] = 5
        for i in range(4, n+1):
            print(i)
            dpList[i] = (2 * dpList[i - 1] + dpList[i - 3]) % mod
        return dpList[n]

thing = Solution()
print(thing.numTilings(99))
