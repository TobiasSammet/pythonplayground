class Solution :
    def isPalindrome(self, s: str) -> bool :
        input: str = s.lower()
        input = self.cleanString(input)
        return self.validPalindrome(input)

    def validPalindrome(self, s: str) -> bool :
        if len(s) <= 1:
            return True
        starter: int = 0
        ender: int = len(s) -1

        while starter < ender :
            if s[starter] != s[ender] :
                return False
            starter += 1
            ender -=1
        return True

    def cleanString(self, s: str) -> str :
        retVal: str = ""
        for c in s:
            if c.isalnum() :
                retVal += c
        return retVal
thing = Solution()
print(thing.isPalindrome('A man, a plan, a canal: Panama')) # true
print(thing.isPalindrome('ab')) # false