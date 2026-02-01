# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#     a, b are from arr
#     a < b
#     b - a equals to the minimum absolute difference of any two elements in arr

# Example 1:
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

# Example 2:
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]

# Example 3:
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
# Constraints:
#     2 <= arr.length <= 10^5
#     -10^6 <= arr[i] <= 10^6
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        length = len(arr)
        retVal: List[List[int]] = []
        if length <= 1:
            return retVal
        arr.sort()
        minDifference = self._calcMinDifference(arr)
        for i in range(0, length -1):
            tempVal: int = arr[i+1] - arr[i]
            if tempVal == minDifference:
                retVal.append([arr[i], arr[i+1]])
        return retVal

    def _calcMinDifference(self, arr: List[int]) -> int:
        length = len(arr)
        retVal: int = float('Inf')
        for i in range(0, length -1):
            retVal = min(retVal, arr[i+1] - arr[i])
        return retVal    
    

def main(): 
    thingy = Solution()
    assert thingy.minimumAbsDifference([4, 2, 1, 3]) == [[1,2],[2,3],[3,4]], "Test Case 1 has failed"
    assert thingy.minimumAbsDifference([1, 3, 6, 10, 15]) == [[1,3]], "Test Case 2 has failed"
    assert thingy.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]) == [[-14,-10],[19,23],[23,27]], "Test Case 3 has failed"

if __name__ == "__main__":
    main()