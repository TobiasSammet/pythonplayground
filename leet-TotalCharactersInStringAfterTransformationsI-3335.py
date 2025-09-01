# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

#     If the character is 'z', replace it with the string "ab".
#     Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.

# Return the length of the resulting string after exactly t transformations.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: s = "abcyy", t = 2

# Output: 7

# Explanation:

#     First Transformation (t = 1):
#         'a' becomes 'b'
#         'b' becomes 'c'
#         'c' becomes 'd'
#         'y' becomes 'z'
#         'y' becomes 'z'
#         String after the first transformation: "bcdzz"
#     Second Transformation (t = 2):
#         'b' becomes 'c'
#         'c' becomes 'd'
#         'd' becomes 'e'
#         'z' becomes "ab"
#         'z' becomes "ab"
#         String after the second transformation: "cdeabab"
#     Final Length of the string: The string is "cdeabab", which has 7 characters.

# Example 2:

# Input: s = "azbk", t = 1

# Output: 5

# Explanation:

#     First Transformation (t = 1):
#         'a' becomes 'b'
#         'z' becomes "ab"
#         'b' becomes 'c'
#         'k' becomes 'l'
#         String after the first transformation: "babcl"
#     Final Length of the string: The string is "babcl", which has 5 characters.



from typing import List

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        freq: List[int] = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        print(freq)
        for i in range(0, t):
            lastOne: int = freq[25]
            firstOne: int = freq[0]
            for j in reversed(range(1,26)):
                freq[j] = freq[j-1]
            freq[0] = lastOne
            freq[1] = (freq[0] + firstOne)
            # print(freq)
        retVal:int = 0
        for value in freq:
            retVal += value
        return retVal % mod
        
    

thing = Solution()
print(thing.lengthAfterTransformations("abcyy", 2))