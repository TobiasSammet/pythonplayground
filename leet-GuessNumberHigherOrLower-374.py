# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

#     -1: Your guess is higher than the number I picked (i.e. num > pick).
#     1: Your guess is lower than the number I picked (i.e. num < pick).
#     0: your guess is equal to the number I picked (i.e. num == pick).

# Return the number that I picked.

# Example 1:

# Input: n = 10, pick = 6
# Output: 6

# Example 2:

# Input: n = 1, pick = 1
# Output: 1

# Example 3:

# Input: n = 2, pick = 1
# Output: 1

# Constraints: 1 <= n <= 231 - 1;
# 1 <= pick <= n;

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num: int) -> int:
    value: int = 6
    if num < value:
        return 1
    if num > value:
        return -1
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        lowerBound: int = 1
        upperBound: int = n
        lastGuess: int = 0
        myGuess = (upperBound + lowerBound) // 2
        while True:
            result: int = guess(myGuess)
            if result == 0:
                return myGuess
            if result == 1:
                lowerBound = myGuess
            if result == -1:
                upperBound = myGuess
            myGuess = (upperBound + lowerBound) // 2
            if lastGuess == myGuess:
                if result == 1:
                    myGuess += 1
                if result == -1:
                    myGuess -= 1
            lastGuess = myGuess

    


def main():
    thingy = Solution()
    print(thingy.guessNumber(10))


if __name__ == "__main__":
    main()