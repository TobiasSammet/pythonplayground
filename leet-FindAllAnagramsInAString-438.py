from typing import List

class Solution:
    #create array with all letters and then remove and add one at a time after we initially fill it to determine anagram
    def findAnagrams(self, s: str, p: str) -> List[int]:
        retVal: List[int] = []
        if len(s) < len(p): 
            return retVal
        sValues: List[int] = [0] * 26
        pValues: List[int] = [0] * 26
        for c in p :
            index: int = (ord(c) - ord('a'))
            pValues[index]+= 1
        
        for i in range(0, len(s)) :
            index: int = ord(s[i]) - ord('a')
            sValues[index] += 1
            if i >= len(p) -1  :
                if self.isAnagram(pValues, sValues) :
                    retVal.append(i - len(p) + 1)
                index = ord(s[i -len(p) + 1]) - ord('a')
                sValues[index] -= 1
        return retVal

    def isAnagram(self, pValues: [int], sValues: [int]) -> bool :
        print(pValues)
        print(sValues)
        print('======')
        for i in range(0,26) :
            if pValues[i] != sValues[i] :
                return False
        return True


thing = Solution()
print(thing.findAnagrams('cbaebabacd', 'abc'))