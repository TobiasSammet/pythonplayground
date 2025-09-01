# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

# Example 1:

# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

# Example 2:

# Input: n = 2
# Output: [1,2]

 

# Constraints:

#     1 <= n <= 5 * 104

from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        retVal: List[int] = [0] * n
        currentValue = 1
        for i in range(n):
            retVal[i] = currentValue
            if currentValue * 10 <= n:
                currentValue *= 10
            else:
                if currentValue >= n:
                    currentValue = currentValue // 10
                currentValue += 1
                while currentValue % 10 == 0:
                    currentValue = (int)(currentValue / 10)

        return retVal

thingy = Solution()

print(thingy.lexicalOrder(34))