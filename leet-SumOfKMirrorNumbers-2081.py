class Solution:
    def kMirror(self, k: int, n: int) -> int:
        if k<=0:
            return 0
        i:int  = 0
        currentNumber: int = 0
        retVal: int = 0

        while(i<n):
            currentNumber += 1
            if self.isPalindrome(str(currentNumber)):
                baseNum = self.convert_to_base_n_iterative(currentNumber, k)
                if self.isPalindrome(str(baseNum)):
                    retVal += currentNumber
                    i += 1

        return retVal

    def isPalindrome(self, s: str) -> bool:
        t = s[::-1]
        return s == t

    def convert_to_base_n_iterative(self, number: int, base: int) -> str:
        result = ''
        while number > 0:
            result = str(number % base) + result
            number //= base
        return result or '0'


thingy = Solution()

print(thingy.kMirror(2,5)) # 25
print(thingy.kMirror(7,17)) # 20379000