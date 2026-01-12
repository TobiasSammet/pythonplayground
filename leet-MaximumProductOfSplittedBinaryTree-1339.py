# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
# Note that you need to maximize the answer before taking the mod and not after taking it.

# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

# Example 2:
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

# Constraints:
#     The number of nodes in the tree is in the range [2, 5 * 104].
#     1 <= Node.val <= 104

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    _maxProd: int = float('-inf')
    _treeSum: int
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self._calcTreeSum(root)
        self._findMaxProduct(root)
        return int(self._maxProd % (10**9 + 7))


        return 0
    def _calcTreeSum(self, root: TreeNode) :
        retVal: int = 0
        nodesToProcess: List[TreeNode] = [root]
        while len(nodesToProcess) > 0:
            currentNode = nodesToProcess.pop()
            retVal += currentNode.val
            if currentNode.left != None:
                nodesToProcess.append(currentNode.left)
            if currentNode.right != None:
                nodesToProcess.append(currentNode.right)
        self._treeSum = retVal
    
    def _findMaxProduct(self, node: Optional[TreeNode]):
        if node == None:
            return 0
        leftSum = self._findMaxProduct(node.left)
        rightSum = self._findMaxProduct(node.right)
        subtreeSum = node.val + leftSum + rightSum
        otherSum = self._treeSum - subtreeSum
        self._maxProd = max(self._maxProd, subtreeSum * otherSum)
        return subtreeSum
    
def buildTree() -> TreeNode:
    root = TreeNode(1)
    root.left =  TreeNode(2)
    root.left.left =  TreeNode(4)
    root.left.right =  TreeNode(5)
    root.right =  TreeNode(3)
    root.right.left =  TreeNode(6)

    return root

def main(): 
    thing = Solution()
    print(thing.maxProduct(buildTree()))

    assert thing.maxProduct(buildTree()) == 110, "Test Case Failed"

if __name__ == "__main__":
    main()