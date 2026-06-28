from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        return False
    

def main():
    thingy = Solution()
    assert thingy.check(nums = [3,4,5,1,2]) ==True, "Test Case Failed"
    assert thingy.check(nums = [2,1,3,4]) ==False, "Test Case Failed"
    assert thingy.check(nums = [1,2,3]) ==True, "Test Case Failed"
    # assert thingy.check() ==True, "Test Case Failed"



if __name__ == "__main__":
    main()