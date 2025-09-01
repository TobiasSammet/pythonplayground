from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) -1
        
        while left <= right :
            pivot: int = left + (right - left) //2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1


thing = Solution()
nums: List[int] = [-9,0,2,6,22,29]
print(thing.search(nums, 29))