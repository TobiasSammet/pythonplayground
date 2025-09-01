# You are given a string word, and an integer numFriends.

# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

#     word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
#     All the split words are put into a box.

# Find the

# string from the box after all the rounds are finished.

 

# Example 1:

# Input: word = "dbca", numFriends = 2

# Output: "dbc"

# Explanation: 

# All possible splits are:

#     "d" and "bca".
#     "db" and "ca".
#     "dbc" and "a".

# Example 2:

# Input: word = "gggg", numFriends = 4

# Output: "g"

# Explanation: 

# The only possible split is: "g", "g", "g", and "g".

 

# Constraints:

#     1 <= word.length <= 5 * 103
#     word consists only of lowercase English letters.
#     1 <= numFriends <= word.length


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        sizeofString: int = len(word) - numFriends + 1
        retVal: str = word[:sizeofString]
        for i in range(len(word)):
            tempString = word[i:i+sizeofString]
            if tempString > retVal:
                # print(tempString)
                retVal = tempString

        return retVal
    
thingy = Solution()

print(thingy.answerString("dcba", 2)) # dcb
print(thingy.answerString("gggg", 4)) # g
print(thingy.answerString("aann", 2)) # nn
print(thingy.answerString("gh", 2)) # h