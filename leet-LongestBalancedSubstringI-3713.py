# You are given a string s consisting of lowercase English letters.
# A of s is called balanced if all distinct characters in the substring appear the same number of times.
# Return the length of the longest balanced substring of s.

# Example 1:
# Input: s = "abbac"
# Output: 4
# Explanation:
# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:
# Input: s = "zzabccy"
# Output: 4
# Explanation:
# The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​

# Example 3:
# Input: s = "aba"
# Output: 2
# Explanation:
# ​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

# Constraints:
#     1 <= s.length <= 1000
#     s consists of lowercase English letters.


from typing import List

class Solution:
    def longestBalanced(self, s: str) -> int:
        length: int = len(s)
        retVal: int = 1
        for i in range(0, length):
            letterArray: List[int] = [0] * 26
            for j in range(i, length):
                tempNum: int = ord(s[j]) - 97
                letterArray[tempNum] += 1
                filtered = list(filter(lambda x: x != 0, letterArray))
                if max(filtered) == min(filtered):
                    retVal = max(retVal, j - i + 1)
        return retVal

def main():
    thingy = Solution()
    assert thingy.longestBalanced("abbac") == 4, "Test case failed"
    assert thingy.longestBalanced("zzabccy") == 4, "Test case failed"
    assert thingy.longestBalanced("aba") == 2, "Test case failed"
    # assert thingy.longestBalanced("abbac") == 4, "Test case failed"


if __name__ == "__main__":
    main()