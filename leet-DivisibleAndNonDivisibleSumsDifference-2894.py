from typing import List

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        arr = [0] * (n + 1)
        for i in range(0, n+1):
            arr[i] = i
        
        num2 = 0
        i = m
        while i <= n:
            num2 += i
            arr[i] = 0
            i += m
        num1 = sum(arr)

        return num1- num2
        

thingy = Solution()

# print(thingy.differenceOfSums(10,3))    # 19
# print(thingy.differenceOfSums(5,6))    # 15
print(thingy.differenceOfSums(5,1))    # -15
