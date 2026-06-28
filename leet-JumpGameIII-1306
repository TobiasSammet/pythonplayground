# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
# Notice that you can not jump outside of the array at any time.

# Example 1:
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3

# Example 2:
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true
# Explanation:
# One possible way to reach at index 3 with value 0 is:
# index 0 -> index 4 -> index 1 -> index 3

# Example 3:
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.

# Constraints:

#     1 <= arr.length <= 5 * 10^4
#     0 <= arr[i] < arr.length
#     0 <= start < arr.length


from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        length = len(arr)
        bfs: List[int] = [start]
        visited: List[bool] = [False] * length
        visited[start] = True
        while len(bfs) >0:
            temp_Bfs: List[int] = []
            for i in range(0, len(bfs)):
                item = bfs[i]
                temp_val = arr[item]
                if temp_val == 0:
                    return True
                plus_val  = item + temp_val
                if plus_val < length and visited[plus_val] == False:
                    temp_Bfs.append(plus_val)
                    visited[plus_val] = True
                neg_val = item - temp_val
                if neg_val >= 0 and visited[neg_val] == False:
                    temp_Bfs.append(neg_val)
                    visited[neg_val] = True
            bfs = temp_Bfs
        return False
    

def main():
    thingy = Solution()
    assert thingy.canReach(arr = [4,2,3,0,3,1,2], start = 5) == True, "Test Case Failed"
    assert thingy.canReach([4,2,3,0,3,1,2], start = 0) == True, "Test Case Failed"
    assert thingy.canReach([3,0,2,1,2], start = 2) == False, "Test Case Failed"
    # assert thingy.canReach() == True, "Test Case Failed"

if __name__ == "__main__":
    main()
