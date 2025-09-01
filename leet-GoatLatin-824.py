from typing import List

class Solution :
    def toGoatLatin(self, s: str) -> str :
        retVal: str = ""
        words: List[str] = s.split(" ")
        i: int = 0
        for word in words:
            i += 1
            if (self.isVowel(word[0])):
                retVal += " " + word + "ma"
            else:
                retVal += " " + word[1:] + word[0] + "ma"
            
            for j in range(0, i):
                retVal += "a"
        return retVal.strip()

    def isVowel(self, c: str) -> bool :
        if c == 'a' or c == 'A':
            return True
        if c == 'e' or c == 'E':
            return True
        if c == 'i' or c == 'I':
            return True
        if c == 'o' or c == 'O':
            return True
        if c == 'u' or c == 'U':
            return True            
            
        return False
thing = Solution()
print(thing.toGoatLatin("I speak Goat Latin"))