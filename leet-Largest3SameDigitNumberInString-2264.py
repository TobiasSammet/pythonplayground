class Solution:

    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            temp: str = f"{i}{i}{i}"
            # print(temp)
            if num.find(temp) >= 0:
                return temp
        return ""

    def mine_largestGoodInteger(self, num: str) -> str:
        retVal: str = ""
        bestVal: int = -1

        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] and num[i - 1] == num[i]:
                temp: str = num[i-2:i+1]
                # print(temp)
                if int(temp) > bestVal:
                    bestVal = int(temp)
                    retVal = temp

        return retVal
    
    
    

thingy = Solution()

print(thingy.largestGoodInteger('6777133339')) # 777
print(thingy.largestGoodInteger('2300019')) # 000
print(thingy.largestGoodInteger('42352338')) # (empty string)
# print(thingy.largestGoodInteger('')) # 
