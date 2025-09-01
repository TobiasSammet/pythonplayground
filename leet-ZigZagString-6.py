class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 1 : 
            return ''
        if numRows == 1 :
            return s
        retVal = ''
        data: [] = [''] * numRows
        iPos: int = 0
        countUp: bool = True
        for c in s :
            data[iPos] = data[iPos] + c
            if countUp: 
                iPos += 1
                if iPos == numRows :
                    countUp = False
                    iPos -= 2
            else :
                iPos -= 1
                if iPos < 0 :
                    countUp = True
                    iPos = 1
        for temp in data:
            retVal += temp
        return retVal


thing = Solution()
result = thing.convert('PAYPALISHIRING', 3)
print(result)
if (result == 'PAHNAPLSIIGYIR') :
    print('Success')
else :
    print('Fail')