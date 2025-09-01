from typing import List

class Solution :
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retVal: List[List[str]] = []
        if len(strs) == 0 : return retVal
        if len(strs) == 1 : 
            retVal.append([strs[0]])
            return retVal
        usedWords: List[str] = []
        for i in range(len(strs)) :
            currentWord: str = strs[i]
            if not currentWord in usedWords :
                newList: List[str] = [currentWord]
                alphaCurrentWord: str = self.alphabetizeString(currentWord)
                for j in range(i + 1, len(strs)) :
                    if self.wordIsAnagram(alphaCurrentWord, strs[j]) :
                        newList.append(strs[j])
                        usedWords.append(strs[j])
                retVal.append(newList)
        return retVal

    def alphabetizeString(self, word: str) -> str :
        return ''.join(sorted(word))
    def wordIsAnagram(self, word1: str, word2:str) -> bool :
        retVal: bool = False
        if len(word1) == len(word2) :
            retVal = (word1 == self.alphabetizeString(word2))
        return retVal

class KeyItem :
    key = ''
    items = []

    def __init__(self,key, value):
        self.key = key
        self.items = []
        self.items.append(value)

class NewSolution(Solution) :
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retVal: List[List[str]] = []
        if len(strs) == 0 : return retVal
        if len(strs) == 1 : 
            retVal.append([strs[0]])
            return retVal
        theList: List[KeyItem] = []
        for word in strs :
            alphaCurrentWord = self.alphabetizeString(word)
            self.findOrAppendItem(theList, alphaCurrentWord, word)

        for item in theList :
            retVal.append(item.items)
        
        return retVal

    #either adds to existing item or creates a new one -- this is very expensive
    def findOrAppendItem(self, theList: List[KeyItem], key: str, value: str) :
        for item in theList :
            if item.key == key:
                item.items.append(value)
                return
        newItem: KeyItem = KeyItem(key, value)            
        theList.append(newItem)

thing = NewSolution()
strs: List[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(thing.groupAnagrams(strs))
