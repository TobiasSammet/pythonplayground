from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        length = len(sorted_list)
        if length <2:
            return False

        for i in range(0, length-1):
            if sorted_list[i] != i+1:
                return False
        if sorted_list[length-1] == sorted_list[length -2]:
            return True

        return False
    

def main():
    thingy = Solution()
    assert thingy.isGood([2, 1, 3]) == False , "Test Case Failed"
    assert thingy.isGood([1, 3, 3, 2]) == True, "Test Case Failed"
    assert thingy.isGood([1,1]) == True, "Test Case Failed"

    assert thingy.isGood([3, 4, 4, 1, 2, 1]) == False, "Test Case Failed"


if __name__ == "__main__":
    main()
    

