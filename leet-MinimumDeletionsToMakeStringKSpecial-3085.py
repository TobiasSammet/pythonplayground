
import math
from typing import List

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        letters: List[int] = [0] * 26
        for i in range(0, len(word)):
            letters[ord(word[i])-97] += 1

        letters.sort()            
        letterCounts: List[int] = []

        for i in range(26):
            if letters[i]!= 0:
                letterCounts.append(letters[i])

        if len(letterCounts) <= 0:
            return 0
        
        retVal = math.inf

        for i in range(len(letterCounts)):
            currentLetterCount = letterCounts[i]
            localReplacements = 0
            for j in range(len(letterCounts)):
                if i != j:
                    tempLetterCount = letterCounts[j]
                    if tempLetterCount < currentLetterCount:
                        localReplacements += tempLetterCount
                    elif tempLetterCount - currentLetterCount > k:
                        localReplacements += tempLetterCount - currentLetterCount - k
            retVal = min(retVal, localReplacements)
        return retVal   
    

thingy = Solution()

print(thingy.minimumDeletions('aabcaba', 0)) # 3
print(thingy.minimumDeletions('dabdcbdcdcd', 2)) #2
print(thingy.minimumDeletions('aaabaaa', 2)) #1