class Solution :
    def detectCapitalUse(self, word: str) -> bool :
        if word == word.lower() or word == word.upper() :
            return True
        temp: str = word[0:1]

        if temp == temp.upper() :
            temp = word[1:]
            if temp == temp.lower() :
                return True
        return False

thing = Solution()
print(thing.detectCapitalUse('USA')) # true
print(thing.detectCapitalUse('leetcode')) # true
print(thing.detectCapitalUse('leetCode')) # false
print(thing.detectCapitalUse('Hello')) # true