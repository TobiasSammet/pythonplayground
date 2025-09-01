from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        odds: int = 0
        evens: int = 0
        alternating: int = 0
        checkOdd: bool = (nums[0]%2 == 1)
        for num in nums:
            if num % 2 == 0:
                evens += 1
                if checkOdd == False:
                    alternating += 1
                    checkOdd = True
            else:
                odds += 1
                if checkOdd == True:
                    alternating += 1
                    checkOdd = False
        return max(evens, odds, alternating)
    

thingy = Solution()

print(thingy.maximumLength([1,2,3,4])) #4
print(thingy.maximumLength([1, 2, 1, 1, 2, 1, 2])) #6
print(thingy.maximumLength([1,3])) #2
print(thingy.maximumLength([1,5,9,4,2])) #3