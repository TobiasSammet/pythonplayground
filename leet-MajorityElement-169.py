from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count: int = len(nums)
        dictionary: dict[int, int] = {}
        for i in range(0, count) :
            if nums[i] in dictionary:
                dictionary[nums[i]] = dictionary.get(nums[i]) + 1
            else:
                dictionary[nums[i]] = 1
            tempVal: int = dictionary.get(nums[i])
            if tempVal > count / 2:
                return nums[i]


thing = Solution()
nums: List[int] = [2, 2, 1, 1, 1, 2, 2]
print(thing.majorityElement(nums))
