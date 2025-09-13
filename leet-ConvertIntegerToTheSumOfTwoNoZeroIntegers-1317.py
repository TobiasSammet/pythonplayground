from typing import List

# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

#     a and b are No-Zero integers.
#     a + b = n

# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

# Example 1:

# Input: n =s 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.

# Example 2:

# Input: n = 11
# Output: [2,9]
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 11 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.

# Constraints:

#     2 <= n <= 104

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n <= 1:
            return []
        i = 1
        while i < n:
            second = n-i
            if  not "0" in str(i) and not "0" in str(second):
                return [i, second]
            i+= 1
        return []


def main():
    thingy = Solution()

    print(thingy.getNoZeroIntegers(2)) # [1,1]
    print(thingy.getNoZeroIntegers(11)) # [2, 9]


if __name__ == "__main__":
    main()