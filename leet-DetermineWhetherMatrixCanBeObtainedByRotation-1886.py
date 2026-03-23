# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
# Example 1:
# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

# Example 2:
# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat.

# Example 3:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

# Constraints:
#     n == mat.length == target.length
#     n == mat[i].length == target[i].length
#     1 <= n <= 10
#     mat[i][j] and target[i][j] are either 0 or 1.


from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if len(mat) == 1:
            return mat[0][0] == target[0][0]
        
        if self.areArraysTheSame(mat, target):
            return True
        
        temp90 = self.rotateArray(mat)
        if self.areArraysTheSame(temp90, target):
            return True
        temp180 = self.rotateArray(temp90)
        if self.areArraysTheSame(temp180, target):
            return True
        temp270 = self.rotateArray(temp180)
        if self.areArraysTheSame(temp270, target):
            return True
        return False
    
    # 90 deg rotation means:
    # mat[i][j] -> mat[j][n-i-1]
    def rotateArray(self, source: List[List[int]]) -> List[List[int]]:
        length = len(source)
        ret_val = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(length):
                ret_val[i][j] = source[j][length - i - 1]
        return ret_val
    
    def areArraysTheSame(self, source: List[List[int]], target: List[List[int]]) -> bool:
        length = len(source)
        for i in range(length):
            for j in range(length):
                if source[i][j] != target[i][j]:
                    return False
        return True
    

def main():
    thingy = Solution()

    assert thingy.findRotation([[0,1],[1,0]], [[1,0],[0,1]]) == True, "Test Case Failed"
    assert thingy.findRotation([[0,1],[1,1]], [[1,0],[0,1]]) == False, "Test Case Failed"
    assert thingy.findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]) == True, "Test Case Failed"
    # assert thingy.findRotation() == True, "Test Case Failed"

if __name__ == "__main__":
    main()