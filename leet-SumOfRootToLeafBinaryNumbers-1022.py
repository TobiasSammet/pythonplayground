# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.
#     For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
# The test cases are generated so that the answer fits in a 32-bits integer.

# Example 1:
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

# Example 2:
# Input: root = [0]
# Output: 0

# Constraints:
#     The number of nodes in the tree is in the range [1, 1000].
#     Node.val is 0 or 1.

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeBuilder:
    def buildBinaryTree(self, arr: Optional[List[int]]) -> Optional[TreeNode]:
        if not arr or len(arr) == 0 or arr[0] is None:
            return None
    
        # Create the root node
        root = TreeNode(arr[0])
    
        # Use a queue to keep track of nodes that need children assigned
        queue = deque([root])
        i = 1
    
        while queue and i < len(arr):
            current = queue.popleft()
            
            # Assign left child
            if i < len(arr) and arr[i] is not None:
                current.left = TreeNode(arr[i])
                queue.append(current.left)
            i += 1
            
            # Assign right child
            if i < len(arr) and arr[i] is not None:
                current.right = TreeNode(arr[i])
                queue.append(current.right)
            i += 1
        
        return root

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if self._isLeaf(root):
            return root.val
        retVal: int = self._calcSum(root, "")
        return retVal
    
    def _calcSum(self, node: TreeNode, currentString: str) -> int:
        currentString += str(node.val)
        if self._isLeaf(node):
            return int(currentString, 2)
        retVal: int = 0
        if node.left != None:
            retVal += self._calcSum(node.left, currentString)
        if node.right != None:
            retVal += self._calcSum(node.right, currentString)
        return retVal
    
    def _isLeaf(self, root: TreeNode) -> bool:
        if root.left == None and root.right == None:
            return True
        return False
    

def main():
    thingy = Solution()
    builder = TreeBuilder()
    root = builder.buildBinaryTree([1,0,1,0,1,0,1])
    assert thingy.sumRootToLeaf(root) == 22, "Test case failed"
    root2 = builder.buildBinaryTree([0])
    assert thingy.sumRootToLeaf(root2) == 0, "Test case failed"

if __name__ == "__main__":
    main()