# Given two positive integers n and k, the binary string Sn is formed as follows:
#     S1 = "0"
#     Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
# For example, the first four strings in the above sequence are:
#     S1 = "0"
#     S2 = "011"
#     S3 = "0111001"
#     S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

# Example 1:
# Input: n = 3, k = 1
# Output: "0"
# Explanation: S3 is "0111001".
# The 1st bit is "0".

# Example 2:
# Input: n = 4, k = 11
# Output: "1"
# Explanation: S4 is "011100110110001".
# The 11th bit is "1".

# Constraints:
#     1 <= n <= 20
#     1 <= k <= 2^n - 1

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        tempString: str = self._generateString(n)
        return tempString[k-1]

    def _generateString(self, n: int) -> str:
        if n <= 0:
            return ""
        ret_val = "0"
        if n == 1:
            return ret_val
        for i in range(1, n):
            temp_str = ret_val

            ret_val = temp_str + "1" + self._processString(temp_str)

        return ret_val
    
    def _processString(self, value: str) -> str :
        # reverse of the inverse
        ret_val: str = ""
        for char in value:
            ret_val += "0" if char == "1" else "1"

        # this reverses the string
        return ret_val[::-1]
            





def main():
    thingy = Solution()
    assert thingy.findKthBit(3,1) == "0", "Test Case Failed"
    assert thingy.findKthBit(4,11) == "1", "Test Case Failed"
    # assert thingy.findKthBit(3,1) == "0", "Test Case Failed"



if __name__ == "__main__":
    main()      