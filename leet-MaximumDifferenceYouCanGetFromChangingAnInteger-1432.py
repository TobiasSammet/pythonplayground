class Solution:
    def maxDiff(self, num: int) -> int:
        theNum: str = str(num)
        minVal: int = num
        maxVal: int = num
        theDigit = ""

        for i in range(0, len(theNum)):
            theDigit = theNum[i]
            if theDigit != '9':
                maxVal = int(theNum.replace(theDigit, '9'))
                break
        
        theDigit = ""
        for i in range(0, len(theNum)):
            theDigit = theNum[i]
            if i == 0:
                if theDigit != '1':
                    minVal = int(theNum.replace(theDigit, '1'))
                    break
            else :
                if (theDigit != '0') and (theDigit != theNum[0]):
                    minVal = int(theNum.replace(theDigit, '0'))
                    break

        # print(maxVal)
        # print(minVal)

        return maxVal - minVal
    
        

thingy = Solution()

print(thingy.maxDiff(123456)) # 820000
# print(thingy.maxDiff(555)) # 888