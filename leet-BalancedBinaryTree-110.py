# Given a binary tree, determine if it is height-balanced.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Constraints:
#     The number of nodes in the tree is in the range [0, 5000].
#     -10^4 <= Node.val <= 10^4

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
    imbalance_found: bool = False
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self._dfs(root)
        return not self.imbalance_found
    
    def _dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        elif self.imbalance_found == False:
            left_depth: int = self._dfs(node.left)
            right_depth: int = self._dfs(node.right)
            if abs(left_depth - right_depth) > 1:
                self.imbalance_found = True
            return 1 + max(left_depth, right_depth)
        return 0


def main(): 
    thing = Solution()
    builder = TreeBuilder()
    root = builder.buildBinaryTree([3, 9, 20, None, None, 15, 7])
    assert thing.isBalanced(root) == True, "Test Case Failed"

if __name__ == "__main__":
    main()