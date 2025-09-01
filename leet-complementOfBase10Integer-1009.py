class Solution:
    def findComplement(self, num: int) -> int:
        result: int = 0
        i: int = 0
        while num > 0 :
            if num % 2 == 0:
                result += pow(2, i)
            i = i + 1
            num = num//2
        return result

thing = Solution()
print(thing.findComplement(5)) # 2
print(thing.findComplement(7)) # 0
print(thing.findComplement(4)) # 3
