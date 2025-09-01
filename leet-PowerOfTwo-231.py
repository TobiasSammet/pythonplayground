class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1: 
            return True
        if n % 2 == 1:
            return False
        
        temp = n
        while temp > 1:
            if temp % 2 == 1:
                return False
            temp = temp / 2
        return True
    

thingy = Solution()


print(thingy.isPowerOfTwo(-8)) # false
print(thingy.isPowerOfTwo(-16)) # false
print(thingy.isPowerOfTwo(1)) # true
print(thingy.isPowerOfTwo(2)) # true
print(thingy.isPowerOfTwo(256)) # true
print(thingy.isPowerOfTwo(255)) # false
print(thingy.isPowerOfTwo(1000)) # false
print(thingy.isPowerOfTwo(128)) # true
# print(thingy.isPowerOfTwo())