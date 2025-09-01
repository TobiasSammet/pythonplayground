class Solution :
    def isPowerOfFour(self, n: int) -> bool :
        if n == 0:
            return False
        while n % 4 == 0:
            n = n / 4

        return n == 1
        
            

thing = Solution()
print(thing.isPowerOfFour(4))
print(thing.isPowerOfFour(21))
print(thing.isPowerOfFour(-2147483648))
print(thing.isPowerOfFour(-64))