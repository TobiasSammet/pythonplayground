from typing import List

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = (10**9+7)
        sums: List[int] = [0] * (n +1)
        sums[0] = 1
        # print(sums)

        for i in range(1, n+1):
            tempVal = pow(i, x)

            if tempVal > n:
                break

            ## bubble up all the possible sums based on the new tempVal
            for j in range(n, tempVal-1, -1):
                # print(j)
                sums[j] = (sums[j] + sums[j - tempVal])
        # print (sums)

        return sums[n] % mod
    

thingy = Solution()

# print(thingy.numberOfWays(10,2)) # 1
# print(thingy.numberOfWays(4,1)) # 2
# print(thingy.numberOfWays(160,3)) # 1

print(thingy.numberOfWays(213,1)) # 55852583



