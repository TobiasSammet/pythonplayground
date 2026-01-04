# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

# Example 1:
# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.

# Example 2:
# Input: nums = [21,21]
# Output: 64

# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 0

# Constraints:
#     1 <= nums.length <= 104
#     1 <= nums[i] <= 105

from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        retVal: int = 0
        myDict = dict()
        for num in nums:
            if num in myDict:
                retVal += myDict.get(num)
            else :
                maxNum = int(math.sqrt(num))
                tempVals: List[int] = [1, num]
                for i in range(2, maxNum+1):
                    if num % i == 0:
                        tempVals.append(i)
                        temp = num // i
                        if temp != i:
                            tempVals.append(temp)
                        if len(tempVals) > 4:
                            break
                if len(tempVals) == 4:
                    temp = sum(tempVals)
                    retVal += temp
                    myDict[num] = temp
        return retVal
    

def main():
    thing = Solution()
    print(thing.sumFourDivisors([21, 4, 7])) # 32
    print(thing.sumFourDivisors([21,21])) # 64
    print(thing.sumFourDivisors([1,2,3,4,5])) # 0

    # assert thing.sumFourDivisors([21, 4, 7]) == 32, "Test Case Failed"


if __name__ == "__main__":
    main()   