from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        length = len(nums)
        if nums[start] == target:
            return 0
        i: int = 1
        
        while True:
            if start - i >= 0 and nums[start-i] == target:
                return i
            if start + i < length and nums[start+i] == target:
                return i
            i += 1


    


def main():
    thingy = Solution()

    assert thingy.getMinDistance(nums = [1,2,3,4,5], target = 5, start = 3) == 1, "Test Case Failed"
    assert thingy.getMinDistance(nums = [1], target = 1, start = 0) == 0, "Test Case Failed"
    assert thingy.getMinDistance([1,1,1,1,1,1,1,1,1,1], target = 1, start = 0) == 0, "Test Case Failed"
    assert thingy.getMinDistance([1,2,2,2,2,2], 1, 5) == 5, "Test Case Failed"
    assert thingy.getMinDistance([2,2,2,2,2,1], 1, 0) == 5, "Test Case Failed"
    # assert thingy.getMinDistance() == 0, "Test Case Failed"
    # assert thingy.getMinDistance() == 0, "Test Case Failed"


if __name__ == "__main__":
    main()