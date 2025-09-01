from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        count: int = 0

        newNums : List[int] = []
        newNums.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                newNums.append(nums[i])
        for i in range(1, len(newNums)-1):
            currentVal = newNums[i]
            if (currentVal > newNums[i-1]) and (currentVal > newNums[i+1]):
                # hill
                count += 1
            if (currentVal < newNums[i-1]) and (currentVal < newNums[i+1]):
                # valley
                count += 1

        
        return count
    
thingy = Solution()

print(thingy.countHillValley([2, 4, 1, 1, 6, 5])) # 3
print(thingy.countHillValley([6, 6, 5, 5, 4, 1])) # 0
# print(thingy.countHillValley())
