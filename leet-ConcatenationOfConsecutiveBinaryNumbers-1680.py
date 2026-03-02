# Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

# Example 1:
# Input: n = 1
# Output: 1
# Explanation: "1" in binary corresponds to the decimal value 1.

# Example 2:
# Input: n = 3
# Output: 27
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal value 27.

# Example 3:
# Input: n = 12
# Output: 505379714
# Explanation: The concatenation results in "1101110010111011110001001101010111100".
# The decimal value of that is 118505380540.
# After modulo 109 + 7, the result is 505379714.

# Constraints:
#     1 <= n <= 105

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo: int = 1e9 + 7
        retVal: int = 0
        bitLength: int = 0
        curPower: int = 0
        tempPower: int = 1
        for i in range(n+1):
            if i == tempPower:
                bitLength += 1
                curPower += 1
                tempPower = pow(2, curPower)
            retVal = int((retVal * pow(2, bitLength) + i ) % modulo)
        return retVal
    

def main():
    thingy = Solution()
    assert thingy.concatenatedBinary(1) == 1, "Test Case Failed"
    assert thingy.concatenatedBinary(3) == 27, "Test Case Failed"
    assert thingy.concatenatedBinary(12) == 505379714, "Test Case Failed"
    assert thingy.concatenatedBinary(1) == 1, "Test Case Failed"
    assert thingy.concatenatedBinary(1) == 1, "Test Case Failed"
    assert thingy.concatenatedBinary(1) == 1, "Test Case Failed"

if __name__ == "__main__":
    main()