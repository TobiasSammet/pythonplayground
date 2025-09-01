# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    maxDiameter: int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDiameter - 1
        self.depth(root)
        return self.maxDiameter - 1

    def depth(self, node: TreeNode) -> int :
        if (not node):
            return 0
        left: int = self.depth(node.left)
        right: int = self.depth(node.right)
        self.maxDiameter = max(self.maxDiameter, left + right + 1)
        return max(left, right) + 1


def BuildTree() -> TreeNode :
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    return root

thing = Solution()
root = BuildTree()
print(thing.diameterOfBinaryTree(root))