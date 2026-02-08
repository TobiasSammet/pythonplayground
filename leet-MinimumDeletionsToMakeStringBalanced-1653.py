# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
# Return the minimum number of deletions needed to make s balanced.

# Example 1:
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

# Example 2:
# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.

# Constraints:
#     1 <= s.length <= 105
#     s[i] is 'a' or 'b'​​.
from typing import List

class Solution:
    def minimumDeletions(self, s: str) -> int:
        length: int = len(s)

        # total counts of a and b
        bCount: int = 0
        aCount: int = 0

        # these form the minimum deletions to get a balanced string
        # count of all a's from the end to the beginning
        countA: List[int] = [0] * length
        #count of all b's from the beginning to the end
        countB: List[int] = [0] * length 
        for i in range(length):
            countB[i] = bCount
            if s[i] == 'b':
                bCount += 1
  

        for i in range(length -1, -1, -1):
            countA[i] = aCount
            if s[i] == 'a':
                aCount += 1
  

        retVal: int = float('inf')
        for i in range(length):
            retVal = min(retVal, countA[i] + countB[i])
  
        return retVal
        
    

def main(): 
    thingy = Solution()
    assert thingy.minimumDeletions("aababbab") == 2, "Test Case Failed"
    assert thingy.minimumDeletions("bbaaaaabb") == 2, "Test Case Failed"

if __name__ == "__main__":
    main()