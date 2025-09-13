class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelCount: int = 0
        for letter in s:
            if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                vowelCount += 1

        if vowelCount == 0:
            return False
        
        # if the number of vowels is odd alice immediately wins
        # if the number of vowels is even alice just selects all but 1 vowel -- bob cannot play
        return True
    
    
    def fasterbutmorecrypticdoesAliceWin(self, s: str) -> bool:

        # if there are any vowels alice wins
        # if the number of vowels is odd alice immediately wins
        # if the number of vowels is even alice just selects all but 1 vowel and bob cannot play
        for letter in s:
            if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                return True
        return False



def main():
    thingy = Solution()

    print(thingy.doesAliceWin("leetcoder")) # True
    print(thingy.doesAliceWin("bbcd")) # False
    
    


if __name__ == "__main__":
    main()        