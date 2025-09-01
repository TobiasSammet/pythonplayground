class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n = n / 3

        return n == 1
    


thingy = Solution()

print(thingy.isPowerOfThree(27)) # True
print(thingy.isPowerOfThree(0)) # False
print(thingy.isPowerOfThree(9)) # True
print(thingy.isPowerOfThree(24)) # False
print(thingy.isPowerOfThree(19682)) # False
# print(thingy.isPowerOfThree())