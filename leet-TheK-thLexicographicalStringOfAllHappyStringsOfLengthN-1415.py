# A happy string is a string that:
#     consists only of letters of the set ['a', 'b', 'c'].
#     s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

# Example 1:
# Input: n = 1, k = 3
# Output: "c"
# Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

# Example 2:
# Input: n = 1, k = 4
# Output: ""
# Explanation: There are only 3 happy strings of length 1.

# Example 3:
# Input: n = 3, k = 9
# Output: "cab"
# Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

# Constraints:
#     1 <= n <= 10
#     1 <= k <= 100
import math

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if n == 0:
            return ""
        total_strings_available = 3 * math.pow(2, n - 1)
        if k > total_strings_available:
            return ""
        ret_val: str
        # first char is a little harder (as it can be a, b, or c)
        if k <= total_strings_available / 3:
            ret_val = "a"
        elif k > 2 * total_strings_available /3:
            ret_val = "c"
        else:
            ret_val = "b"
        if n > 1:
            bin_str: str = bin(k -1)[2:].zfill(n+1)
            for i in range(len(bin_str) - n + 1, n+1):
                ret_val += self._getNextLetter(ret_val[len(ret_val)-1], bin_str[i])

        return ret_val
    
    def _getNextLetter(self, prev_letter: str, next_digit: str):
        if prev_letter == "a":
            if next_digit == "0":
                return "b"
            return "c"
        if prev_letter == "b":
            if next_digit == "0":
                return "a"
            return "c"
        # "c"
        if next_digit == "0":
            return "a"
        return "b"
    


def main() :
    thingy = Solution()
    assert thingy.getHappyString(1,3) == "c", "Test Case Failed"
    assert thingy.getHappyString(1,4) == "", "Test Case Failed"
    assert thingy.getHappyString(3,9) == "cab", "Test Case Failed"
    assert thingy.getHappyString(10, 100) == "abacbabacb", "Test Case Failed"
    # assert thingy.getHappyString() == "", "Test Case Failed"

if __name__ == "__main__":
    main()