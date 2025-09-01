class Solution:
    def possibleStringCount(self, word: str) -> int:
        retVal: int = 1
        currentLetter: str = word[0]
        i: int = 1
        while i < len(word):
            if currentLetter == word[i]:
                currentLetterCount: int = 1
                while i < len(word) and word[i] == currentLetter:
                    currentLetterCount += 1
                    i += 1
                retVal += currentLetterCount -1
            else :
                currentLetter = word[i]
                i += 1
        return retVal
    

thingy = Solution()

print(thingy.possibleStringCount("abbcccc")) # 5
print(thingy.possibleStringCount("abcd")) # 1
print(thingy.possibleStringCount("aaaa")) # 4
print(thingy.possibleStringCount("ere")) # 1