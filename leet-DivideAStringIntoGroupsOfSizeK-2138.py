from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        retVal: List[str] = []
        currentString: str = ""
        for i in range(0, len(s)):
            currentString += s[i]
            if (i+1) % k == 0:
                retVal.append(currentString)
                currentString = ""
        if currentString != "":
            for i in range(len(currentString), k):
                 currentString += fill
            retVal.append(currentString)
        return retVal
    


thingy = Solution()

print(thingy.divideString("abcdefghi", 3, "x")) # ["abc","def","ghi"]
print(thingy.divideString("abcdefghij", 3, "x")) # ["abc","def","ghi"]
# print(thingy.divideString())
# print(thingy.divideString())
# print(thingy.divideString())