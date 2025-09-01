from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        if root is None:
            return False
        if root.left is None or root.right is None :
            return False
        myQueue: List[TreeNode] = []
        myQueue.append(root.left)
        myQueue.append(root.right)
        return self.processLevel(myQueue, x, y)

    def processLevel(self, level: List[TreeNode], x: int, y: int) -> bool:
        found : int = 0
        if len(level) == 0:
            return False
        nextLevel: List[TreeNode] = []
        for current in level:
            if not current is None:
                if self.hasValue(current, x, y):
                    found += 1
                nextLevel.append(current.left)
                nextLevel.append(current.right)
        if found == 0:
            return self.processLevel(nextLevel, x, y)
        if found == 1:
            return False
        if found == 2:
            return True
        return False

    def hasValue(self, root: TreeNode, x: int, y: int) -> bool:
        if not root.left is None:
            if root.left.val == x or root.left.val == y :
                return True
        if not root.right is None:
            if root.right.val == x or root.right.val == y :
                return True
        return False

def buildTree(x: int) -> TreeNode :
    root: TreeNode = None
    if x == 1:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right = TreeNode(3)
    if x == 2:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)
    if x == 3:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right = TreeNode(3)
    if x == 4: 
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(6)
        root.right.right.left.right = TreeNode(8)
        root.right.right.right.right = TreeNode(9)
    return root

thing = Solution()
print(thing.isCousins(buildTree(1), 4, 3)) # false
print(thing.isCousins(buildTree(2), 4, 5)) # true
print(thing.isCousins(buildTree(3), 2, 3)) # false
print(thing.isCousins(buildTree(4), 8, 9)) # true