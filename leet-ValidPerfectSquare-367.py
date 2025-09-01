class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i: int = 1
        while num > 0:
            num -= i
            i+=2

        return (num == 0)
thing = Solution()
print(thing.isPerfectSquare(1))
print(thing.isPerfectSquare(4))
print(thing.isPerfectSquare(9))
print(thing.isPerfectSquare(100))
print(thing.isPerfectSquare(101)) #false
print(thing.isPerfectSquare(2147483647)) #false