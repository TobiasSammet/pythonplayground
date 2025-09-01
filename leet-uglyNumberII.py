from typing import List

class Solution :
    def nthUglyNumber(self, n: int) -> int :
        if n < 6:
            return n
        t2: int = 0
        t3: int = 0
        t5: int = 0
        uglyNumbers: List[int] = [1] * n
        for i in range(1,n):
            uglyNumbers[i] = min(uglyNumbers[t2]*2, uglyNumbers[t3]*3,uglyNumbers[t5]*5)
            if uglyNumbers[i] == uglyNumbers[t2]*2:
                t2+=1
            if uglyNumbers[i] == uglyNumbers[t3]*3:
                t3+=1
            if uglyNumbers[i] == uglyNumbers[t5]*5:
                t5+=1
        return uglyNumbers[n-1]

thing = Solution()
print(thing.nthUglyNumber(10)) # 12
print(thing.nthUglyNumber(11)) # 15