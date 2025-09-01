from itertools import accumulate 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = ransomNote.replace(' ', '')
        magazine = magazine.replace(' ', '')
        if ransomNote == '' :
            return True
        if magazine == '' :
            return False
        if len(ransomNote) > len(magazine) :
            return False
        magazine = self.sortString(magazine)
        ransomNote = self.sortString(ransomNote)
        print(ransomNote)
        print(magazine)
        
        iPos: int = -1
        for c in ransomNote:
            tempPos: int = magazine.find(c, iPos + 1)
            print(c + ' - ' + str(tempPos))
            if tempPos  == -1 :
                return False
            iPos = tempPos

        return True
    def sortString(self, value: str): 
        return ''.join(sorted(value)) 

thing = Solution()
print(thing.canConstruct('t at','matt'))