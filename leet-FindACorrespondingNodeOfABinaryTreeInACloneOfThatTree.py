# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:

        if original is None or target is None:
            return None
        if cloned.val == target.val:
            return cloned

        return self.findIt(cloned, target.val)

    def findIt(self, root: TreeNode, value: int) -> TreeNode:
        if root.left == None and root.right == None:
            return None
        if root.left != None and root.left.val == value:
            return root.left
        if root.right != None and root.right.val == value:
            return root.right
        temp: TreeNode = None
        if root.left != None:
            temp = self.findIt(root.left, value)
        if temp != None:
            return temp

        if root.right != None:
            temp = self.findIt(root.right, value)

        return temp


def buildTree() -> TreeNode:
    root = TreeNode

    root.val = 7
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(19)
    return root


thing = Solution()
original = buildTree()
print(thing.getTargetCopy(original, buildTree(), original.right.right))
