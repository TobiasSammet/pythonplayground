class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: 
            return False
        word = word.lower()
        hasVowel: bool = False
        hasConsonant: bool = False
        for currentCharacter in word:
            if self.validCharacter(currentCharacter):
                if self.isDigit(currentCharacter) == False:
                    if hasVowel == False or hasConsonant == False:
                        charIsVowel = self.isVowel(currentCharacter)
                        if hasVowel == False:
                            hasVowel = charIsVowel
                        if hasConsonant == False:
                            hasConsonant = not charIsVowel
            else:
                return False
        return hasVowel and hasConsonant
    
    def isDigit(self, char: str) -> bool: 
        ordVal = ord(char)
        if ordVal >= 48 and ordVal <= 57:
            return True
        return False
    
    def isVowel(self, char: str) -> bool: 
        
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            return True
        return False
    
    def validCharacter(self, char: str) -> bool:
        ordVal = ord(char)
        if ordVal >= 97 and ordVal <= 122:
            return True
        return self.isDigit(char)


thingy = Solution()


print(thingy.isValid("234Adas")) # True
print(thingy.isValid("b3")) # False
print(thingy.isValid("a3$e")) # False
print(thingy.isValid("Uue6")) # False
# print(thingy.isValid(""))
