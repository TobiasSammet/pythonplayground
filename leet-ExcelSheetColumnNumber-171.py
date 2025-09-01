class Solution :
    def titleToNumber(self, s: str) -> int :
        if len(s) == 0:
            return 0
        retVal: int = 0
        valueOfA: int = ord('A')
        i: int = 0
        for c in s:
            temp: int = ord(c) - valueOfA + 1
            if i > 0 :
                retVal = retVal * 26 + temp
            else :
                retVal += temp
            i += 1
        return retVal

thing = Solution()
print(thing.titleToNumber('A'))
print(thing.titleToNumber('Z'))
print(thing.titleToNumber('AB'))
print(thing.titleToNumber('ZY'))