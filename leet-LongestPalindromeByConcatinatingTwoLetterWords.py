# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.

 

# Example 1:

# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.

# Example 2:

# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.

# Example 3:

# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is "xx".

 

# Constraints:

#     1 <= words.length <= 105
#     words[i].length == 2
#     words[i] consists of lowercase English letters.

# we know there are only 26*26 combinations of 2 letters so we create a 2d array for these
# and then deal with aa -- if it is odd we can slide it in the middle too!

from typing import List

class Solution:
    
    def longestPalindrome(self, words: list[str]) -> int:
        retVal = 0
        has_a_middle = False
        rows, cols = (26, 26)
        arr = [[0 for _ in range(cols)] for _ in range(rows)]
        for word in words:
            x = ord(word[0]) - ord('a')
            y  = ord(word[1]) - ord('a')
            arr[x][y] += 1

        for i in range(0, 26):
            for j in range(0,26):
                if arr[i][j] > 0:
                    if i != j:
                        maxValue = min(arr[i][j], arr[j][i])
                        # print(i, j, maxValue, arr[i][j], arr[j][i])
                        retVal += 4 * maxValue
                        arr[i][j] = 0
                        arr[j][i] = 0
                    else:
                        retVal += 4 * (arr[i][j] // 2)
                        if arr[i][j] % 2 == 1:
                            has_a_middle = True

        if has_a_middle:
            retVal += 2
        return retVal
    

thingy = Solution()
print(thingy.longestPalindrome(["lc","cl","gg"])) # 6
print(thingy.longestPalindrome(["lc","cl","gg", "gg"])) # 8
print(thingy.longestPalindrome(["ab","ty","yt","lc","cl","ab"])) # 8
print(thingy.longestPalindrome(["cc","ll","xx"])) # 2

