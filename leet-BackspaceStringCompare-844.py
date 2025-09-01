class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if S == T: 
            return True
        if not S or not T :
            return False
        tempS: str = self.processString(S)
        tempT: str = self.processString(T)

        return tempS == tempT
    
    def processString(self, input: str) -> str :
        retVal: str = input
        try: 
            tempPos: int = retVal.index('#')
            while tempPos >= 0 :
                if tempPos == 0 :
                    retVal = retVal[1:]
                else :
                    retVal = retVal[0: tempPos -1] + retVal[tempPos + 1:]
                tempPos = retVal.index('#')

        except Exception:
            tempPos = -1
        return retVal
thing = Solution()

print(thing.backspaceCompare("a##c", "#a#c")                        )