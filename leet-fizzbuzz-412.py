from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        retVal:List[str] = []
        temp: str
        for i in range(1, n + 1):
            temp = ""
            if i%3 == 0:
                temp += "fizz"
            if i%5 == 0: 
                temp += "buzz"
            if temp == "":
                temp = str(i)
            retVal.append(temp)

        return retVal

thing = Solution()
print(thing.fizzBuzz(15))