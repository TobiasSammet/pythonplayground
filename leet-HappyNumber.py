class Solution:
    pastNumbers = []
    def isHappy(self, n: int) -> bool:
        if n == 0: 
            return False
        if self.pastNumbers.count(n) > 0 :
            return False
        self.pastNumbers.append(n)
        sum = 0
        while n > 0:
            if n < 10 :
                sum += (n * n)
                n = 0
            else :
                firstNumber = n % 10
                sum += (firstNumber * firstNumber)
                n = n // 10
        if sum == 1: 
            return True
        else :
            print(sum)
            return self.isHappy(sum)

thing = Solution()
# 10 should be true
print(thing.isHappy(10))
