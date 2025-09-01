class Solution:
    def kthCharacter(self, k: int) -> str:
        word: str = "a"
        for i in range(k):
            tempWord: str = ""
            for j in range(len(word)):
                tempVal: int = ord(word[j]) + 1
                if tempVal == 123:
                    tmepVal = 97
                temp: str = chr(tempVal)
                tempWord += temp
            word += tempWord
            if len(word) >= k:
                return word[k-1]


        return word[k-1]


thingy = Solution()

print(thingy.kthCharacter(1)) # a
print(thingy.kthCharacter(5)) # b
print(thingy.kthCharacter(10)) # c

