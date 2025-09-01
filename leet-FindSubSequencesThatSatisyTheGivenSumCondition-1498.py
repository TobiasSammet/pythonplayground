from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = (10**9+7)
        nums.sort()
        thePowers :List[int] = []
        thePowers.append(1)
        for i in range(1, len(nums)):
            thePowers.append((2 * thePowers[i-1])% mod)
        print(thePowers)
        first: int = 0
        last: int = len(nums)-1
        retVal: int = 0
        while first <= last:
            if (nums[first] + nums[last] <= target):
                retVal += thePowers[last-first]
                first += 1
            else:
                last -= 1
        
        
        return retVal % mod

thingy = Solution()
print(thingy.numSubseq([2, 3, 3, 4, 6, 7], 12)) #61
