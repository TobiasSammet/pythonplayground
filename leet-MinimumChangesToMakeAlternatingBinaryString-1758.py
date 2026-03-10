# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
# Return the minimum number of operations needed to make s alternating.

# Example 1:
# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.

# Example 2:
# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.

# Example 3:
# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".

# Constraints:
#     1 <= s.length <= 104
#     s[i] is either '0' or '1'.

class Solution:
    def minOperations(self, s: str) -> int:
        length: int = len(s)
        if length <= 1:
            return 0
        one_count: int = 0
        zero_count: int = 0
        for i in range(length):
            tempVal: str = s[i]
            if tempVal == "0":
                if i % 2 == 0:
                    one_count += 1
                else:
                    zero_count += 1
            else: 
                if i % 2 == 0:
                    zero_count += 1
                else:
                    one_count += 1

        return min(one_count, zero_count)
    
def main():
    thingy = Solution()
    assert thingy.minOperations("0100") == 1, "Test Case Failed"
    assert thingy.minOperations("10") == 0, "Test Case Failed"
    assert thingy.minOperations("1111") == 2, "Test Case Failed"
    # assert thingy.minOperations("") == 0, "Test Case Failed"
    



if __name__ == "__main__":
    main()      