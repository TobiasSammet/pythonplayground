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
        result = self._addTheBinary(a, b).lstrip("0")
        if result == "":
            result = "0"
        return result
    def _addTheBinary(self, a: str, b:str) -> str:
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


def main():
    thing = Solution()
    # assert thing.addBinary("11", "1") == "100", "Test Case Failed"
    # assert thing.addBinary("1010", "1011") == "10101", "Test Case Failed"
    # assert thing.addBinary("", "") == "", "Test Case Failed"
    # assert thing.addBinary("", "1001") == "1001", "Test Case Failed"
    assert thing.addBinary("0", "0") == "0", "Test Case Failed"

if __name__ == "__main__":
    main()