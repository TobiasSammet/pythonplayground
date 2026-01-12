# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Example 1:
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# Example 2:
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2

# Constraints:
#     The number of nodes in the tree is in the range [1, 104].
#     -105 <= Node.val <= 105

from typing import List, Optional
import math


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        currentNodes: List[TreeNode] = [root]
        nextNodes: List[TreeNode] = []
        currentSum: int = 0
        currentLevel: int = 0
        bestLevel: int = 0
        bestSum: int = -math.inf
        while len(currentNodes) > 0:
            currentLevel += 1
            currentSum = 0
            nextNodes = []
            for node in currentNodes:
                currentSum += node.val
                if node.left != None:
                    nextNodes.append(node.left)
                if node.right != None:
                    nextNodes.append(node.right)
            if currentSum > bestSum:
                bestSum = currentSum
                bestLevel = currentLevel
            currentNodes = nextNodes

        return bestLevel


def buildTree1161() -> TreeNode:
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)
    return root


def buildTree1161partDeux() -> TreeNode:
    root = TreeNode(989)
    root.right = TreeNode(10250)
    root.right.left = TreeNode(98693)
    root.right.right = TreeNode(-89388)
    root.right.right.right = TreeNode(-32127)
    return root


def main():
    thingy = Solution()
    print(thingy.maxLevelSum(None))  # 2
    print(thingy.maxLevelSum(buildTree1161()))  # 2
    print(thingy.maxLevelSum(buildTree1161partDeux()))  # 2

    assert thingy.maxLevelSum(buildTree1161()) == 2, "Test Case Failed"


if __name__ == "__main__":
    main()
