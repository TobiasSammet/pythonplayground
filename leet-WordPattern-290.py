from typing import List

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        AllWords : List[str] = []
        lookup = [""] * 26
        words = str.split(' ')
        i: int = 0
        for c in pattern:
            if i >= len(words):
                return False
            word: str = words[i]
            charValue: int = ord(c) - ord('a')
            if charValue > 25:
                return False
            if lookup[charValue] == "":
                if word in AllWords:
                    return False
                lookup[charValue] = word
                AllWords.append(word)
            else :
                if word != lookup[charValue]:
                    return False
            i += 1
        
        if i < len(words) :
            return False
        
        return True


thingy = Solution()
print(thingy.wordPattern("abba","dog cat cat dog"))
print(thingy.wordPattern("abba","dog cat cat fish"))
print(thingy.wordPattern("aaaa","dog cat cat dog"))
print(thingy.wordPattern("abba","dog dog dog dog"))
print(thingy.wordPattern("aaa","aa aa aa aa"))
print(thingy.wordPattern("jquery","jquery"))