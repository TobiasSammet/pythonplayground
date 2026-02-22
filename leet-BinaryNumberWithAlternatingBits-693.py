# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

# Example 1:
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101

# Example 2:
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.

# Example 3:
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.

# Constraints:
#     1 <= n <= 2^31 - 1
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 0:
            return True
        onOne: bool = True
        tempStr = bin(n)
        tempStr = tempStr[2:]
        for i in range(len(tempStr)):
            tempDigit = tempStr[i]
            if onOne and tempDigit == "0":
                return False
            if onOne == False and tempDigit == "1":
                return False
            onOne = not onOne

        return True
    

def main():
    thingy = Solution()
    assert thingy.hasAlternatingBits(5) == True, "Test Case Failed"
    assert thingy.hasAlternatingBits(7) == False, "Test Case Failed"
    assert thingy.hasAlternatingBits(11) == False, "Test Case Failed"
    # assert thingy.hasAlternatingBits() == True, "Test Case Failed"

if __name__ == "__main__":
    main()