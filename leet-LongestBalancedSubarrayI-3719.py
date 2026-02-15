from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        length = len(nums)
        retVal: int = 0

        for i in range(0, length):
            oddSet = set()
            evenSet = set()
            for j in range(i, length):
                tempNum: int = nums[j]
                if tempNum % 2 == 0:
                    evenSet.add(tempNum)
                else:
                    oddSet.add(tempNum)

                if len(evenSet) == len(oddSet):
                    retVal = max(retVal, j - i + 1)
        
        return retVal
    

def main(): 
    thing = Solution()
    
    
    assert thing.longestBalanced([1, 7, 2, 5, 4, 3]) == 4, "Test Case Failed"
    assert thing.longestBalanced([3, 2, 2, 5, 4]) == 5, "Test Case Failed"
    assert thing.longestBalanced([1, 2, 3, 2]) == 3, "Test Case Failed"
    assert thing.longestBalanced([6, 6]) == 0, "Test Case Failed"
    # assert thing.longestBalanced() == 0, "Test Case Failed"

if __name__ == "__main__":
    main()
