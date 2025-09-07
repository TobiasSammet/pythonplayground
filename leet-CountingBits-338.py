# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# Constraints:

#     0 <= n <= 105


from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        retVal: List[int] = [0] * (n+1)
        if n < 1:
             return retVal;
        retVal[1] = 1
        for i in range (2, n+1) :
            temp = bin(i)            
            temp = temp[2:]
            tempVal: int = 0
            while len(temp) > 0:
                if temp[0] == "1":
                    tempVal += 1
                temp = temp[1:]
            retVal[i] = tempVal

        return retVal


def main():
    thingy = Solution()
    print(thingy.countBits(5)) # [0,1,1,2,1,2]
    

if __name__ == "__main__":
    main()        