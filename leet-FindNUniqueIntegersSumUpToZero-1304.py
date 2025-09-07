from typing import List

# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Example 1:
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

# Example 2:
# Input: n = 3
# Output: [-1,0,1]

# Example 3:
# Input: n = 1
# Output: [0]

# Constraints:
#     1 <= n <= 1000


class Solution:
    def sumZero(self, n: int) -> List[int]:
        retVal: List[int] = []
        maxValue = (n  // 2) + 1
        for i in range(1, maxValue):
            retVal.append(i)
            retVal.append(-i)

        if len(retVal) != n:
            retVal.append(0)
        return retVal



def main():
    thingy = Solution()

    print(thingy.sumZero(5))
    print(thingy.sumZero(3))
    print(thingy.sumZero(1))
    print(thingy.sumZero(6))
    # print(thingy.sumZero())
    # print(thingy.sumZero())
    
    



if __name__ == "__main__":
    main()