# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

# Example 1:
# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).

# Example 2:
# Input: n = 10
# Output: 4
# Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

# Constraints:
#     1 <= n <= 250


import math

class Solution:
    def countTriples(self, n: int) -> int:
        retVal: int = 0
        for i in range(1, n):
            for j in range(1, n):
                value = i * i + j * j
                sqrtValue: int = math.sqrt(value)
                if sqrtValue <= n and sqrtValue.is_integer():
                    retVal += 1



        return retVal
    

def main():
    thingy = Solution()
    print(thingy.countTriples(5)) # 2
    print(thingy.countTriples(10)) # 4
    # print(thingy.countTriples()) # 

if __name__ == "__main__":
    main()