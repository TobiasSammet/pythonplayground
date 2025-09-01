from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        retVal: str = ""
        if len(shift) == 0 :
            return s
        if s == "":
            return s
        # -1 for left and 1 for right
        shiftValue:int = 0            
        for value in shift:
            if value[0] == 0:
                shiftValue -= value[1]
            else :
                shiftValue += value[1]
        if shiftValue < 0:
            retVal = self.shiftLeft(s, abs(shiftValue))
        elif shiftValue > 0:
            retVal = self.shiftRight(s, shiftValue)
        return retVal

    def shiftLeft(self, s: str, length: int) -> str:
        retVal: str = ""
        if length > len(s):
            length = length % len(s)
        print(length)
        retVal = s[-1 * length] + s[: -1 * length]
        return retVal 

    def shiftRight(self, s: str, length: int) -> str:
        retVal: str = ""
        if length > len(s):
            length = length % len(s)
        iPos: int = len(s) - length
        retVal = s[-1 * iPos:] + s[: -1 * iPos]
        return retVal

thing = Solution()
shift: List[List[int]] = []
shift.append([0,1])
shift.append([1,2])
#print(thing.shiftLeft('abc', 1))
print(thing.shiftRight('abc', 1))
print(thing.stringShift('abc', shift))