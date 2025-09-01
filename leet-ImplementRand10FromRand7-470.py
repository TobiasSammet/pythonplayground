from random import randrange


class SolBase: 
    def Rand7(self) -> int :
        return (randrange(10)+ 1)
    

class Solution(SolBase):
    def rand10(self):
        result: int = 0
        for i in range(10):
            result = result + self.Rand7()
        return (result % 10) + 1
        

thing = Solution()
for i in range(10):
    print(thing.rand10())