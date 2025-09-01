# You are given a string s consisting of lowercase English letters.

# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

#     a1 has an odd frequency in the string.
#     a2 has an even frequency in the string.

# Return this maximum difference.

 

# Example 1:

# Input: s = "aaaaabbc"

# Output: 3

# Explanation:

#     The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
#     The maximum difference is 5 - 2 = 3.

# Example 2:

# Input: s = "abcabcab"

# Output: 1

# Explanation:

#     The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
#     The maximum difference is 3 - 2 = 1.



from typing import List

class Solution:
    def maxDifference(self, s: str) -> int:
        if len(s) <=1:
            return len(s)
        letters: List[int] = [0] * 26
        for letter in s:
            tempVal = ord(letter) - 97
            letters[tempVal] += 1
        
        maxOdd = 0
        minEven = len(s)

        for i in range(26):
            if letters[i] != 0:
                if letters[i] % 2 == 1:
                    maxOdd = max(maxOdd, letters[i])
                else:
                    minEven = min(minEven, letters[i])
        
        return maxOdd - minEven
        
    

thingy = Solution()

print(thingy.maxDifference("aaaaabbc"))