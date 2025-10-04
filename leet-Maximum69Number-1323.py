class Solution:
    def maximum69Number (self, num: int) -> int:
        temp: str = str(num)
        for i in range(0, len(temp)):
            if temp[i] == "6":
                retVal: str = temp[0:i] + "9" + temp[i+1:]
                return int(retVal)
        return num

thingy = Solution()

print(thingy.maximum69Number(9669)) # 9969
print(thingy.maximum69Number(9996)) # 9999
print(thingy.maximum69Number(9999)) # 9999
# print(thingy()) #