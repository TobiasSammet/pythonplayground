class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = str(x)
        if len(temp) == 1:
            return True
        # compare to the string reversed
        return temp == temp[::-1]
    

thingy = Solution()

print(thingy.isPalindrome(121)) # true
print(thingy.isPalindrome(-121)) # false
print(thingy.isPalindrome(10)) # false
# print(thingy.isPalindrome())