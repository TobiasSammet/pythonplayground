# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].

# Constraints:
#     0 <= low <= high <= 10^9

class Solution:
    def slowcountOdds(self, low: int, high: int) -> int:
        retVal: int = 0
        for i in range(low, high+1):
            if i % 2 == 1:
                retVal += 1
        
        return retVal
    
    def countOdds(self, low: int, high: int) -> int:
        startOdd: bool = low % 2 == 1
        endOdd: bool = high % 2 == 1

        if low == high:
            if startOdd:
                return 1
            return 0
        
        retVal = (int)((high - low) / 2)
        if startOdd and endOdd:
            retVal += 1
        if startOdd and not endOdd:
            retVal += 1
        if not startOdd and endOdd:
            retVal += 1

        return retVal
    


def main():
    thingy = Solution()
    print(thingy.countOdds(3, 7)) # 3
    print(thingy.countOdds(8, 10)) # 1
    print(thingy.countOdds(798273637, 970699661)) # 86213013
    # print(thingy.countOdds()) # 

if __name__ == "__main__":
    main()