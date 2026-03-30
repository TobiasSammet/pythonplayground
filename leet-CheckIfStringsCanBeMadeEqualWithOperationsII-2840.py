# You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
#     Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

# Example 1:
# Input: s1 = "abcdba", s2 = "cabdab"
# Output: true
# Explanation: We can apply the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
# - Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
# - Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

# Example 2:
# Input: s1 = "abe", s2 = "bea"
# Output: false
# Explanation: It is not possible to make the two strings equal.

# Constraints:

#     n == s1.length == s2.length
#     1 <= n <= 10^5
#     s1 and s2 consist only of lowercase English letters.

from typing import List

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        odds1: List[str] = []
        odds2: List[str] = []
        evens1: List[str] = []
        evens2: List[str] = []

        length: int = len(s1)

        for i in range(length):
            if i % 2 == 0:
                evens1.append(s1[i])
                evens2.append(s2[i])
            else:
                odds1.append(s1[i])
                odds2.append(s2[i])

        odds1.sort()
        odds2.sort()
        evens1.sort()
        evens2.sort()

        length_odds = len(odds1)
        for i in range(0, len(evens1)):
            if evens1[i] != evens2[i]:
                return False
            if i < length_odds:
                if odds1[i] != odds2[i]:
                    return False
            
        return True

def main():
    thingy = Solution()
    # assert thingy.checkStrings("abcdba", "cabdab") == True, "Test Case Failed"
    # assert thingy.checkStrings("abe", "bea") == False, "Test Case Failed"
    # assert thingy.checkStrings("kvwdssgl", "wskxsdgv") == False, "Test Case Failed"
    assert thingy.checkStrings("z", "u") == False, "Test Case Failed"
    # assert thingy.checkStrings() == True, "Test Case Failed"
    

if __name__ == "__main__":
    main()