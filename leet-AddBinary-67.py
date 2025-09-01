class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0 and len(b) == 0:
            return ""
        if len(a) == 0 :
            return b
        if len(b) == 0:
            return a
        maxlen: int = max(len(a), len(b)) + 1
        a = a.zfill(maxlen)
        b = b.zfill(maxlen)
        result = self.addTheBinary(a, b).lstrip("0")

        return result
    def addTheBinary(self, a: str, b:str) -> str:
        # reverse the strings
        a = a[::-1]
        b = b[::-1]
        retVal: str = ""
        carry: bool = False
        for i in range(len(a)):
            if carry:
                if b[i] == '0' and a[i] == '0' :
                    retVal = "1" + retVal
                    carry = False
                if b[i] == '1' and a[i] == '0' :
                    retVal = "0" + retVal
                if b[i] == '0' and a[i] == '1' :
                    retVal = "0" + retVal
                if b[i] == '1' and a[i] == '1' :
                    retVal = "1" + retVal
            else :
                if b[i] == '0' and a[i] == '0' :
                    retVal = "0" + retVal
                if b[i] == '1' and a[i] == '0' :
                    retVal = "1" + retVal
                if b[i] == '0' and a[i] == '1' :
                    retVal = "1" + retVal
                if b[i] == '1' and a[i] == '1' :
                    retVal = "0" + retVal
                    carry = True
        return retVal[::1]

thing = Solution()
a: str = "0010"
b: str = "1011"


print(thing.addBinary(a,b))