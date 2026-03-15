# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
#     For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement.

# Example 1:
# Input: n = 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

# Example 2:
# Input: n = 7
# Output: 0
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

# Example 3:
# Input: n = 10
# Output: 5
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

# Constraints:
#     0 <= n < 10^9

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_str = bin(n)[2:]
        bin_str = bin_str.replace("0", "2")
        bin_str = bin_str.replace("1", "0")
        bin_str = bin_str.replace("2", "1")
        return int(bin_str, 2)

    def xfindComplement(self, num: int) -> int:
        result: int = 0
        i: int = 0
        while num > 0 :
            if num % 2 == 0:
                result += pow(2, i)
            i = i + 1
            num = num//2
        return result


def main():
    thingy = Solution()
    assert thingy.bitwiseComplement(5) == 2, "Test Case Failed"
    assert thingy.bitwiseComplement(7) == 0, "Test Case Failed"
    assert thingy.bitwiseComplement(4) == 3, "Test Case Failed"
    # assert thingy.bitwiseComplement() == 2, "Test Case Failed"


if __name__ == "__main__":
    main()         