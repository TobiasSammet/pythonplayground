# You are given two integers numBottles and numExchange.
# numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:
#     Drink any number of full water bottles turning them into empty bottles.
#     Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.

# Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.
# Return the maximum number of water bottles you can drink.

# Example 1:
# Input: numBottles = 13, numExchange = 6
# Output: 15
# Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

# Example 2:
# Input: numBottles = 10, numExchange = 3
# Output: 13
# Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

# Constraints:

#     1 <= numBottles <= 100
#     1 <= numExchange <= 100

# DIFFERENCE WITH THIS ONE AND 1518 is that the exchange rate goes up by 1 every time you exchange emply bottles for full ones

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        retVal: int = numBottles
        emptyBottles: int = numBottles
        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            numExchange += 1
            retVal += 1
            emptyBottles += 1

        return retVal
    




def main():
    thingy = Solution()
    print(thingy.maxBottlesDrunk(13,6)) # 15
    print(thingy.maxBottlesDrunk(10,3)) # 13
    # print(thingy.maxBottlesDrunk()) # 


if __name__ == "__main__":
    main()
