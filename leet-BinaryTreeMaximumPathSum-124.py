# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_sum: int
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = 0
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, root: TreeNode) -> int:
        if root is None: 
            return 0
        leftGain: int = max(self.max_gain(root.left), 0)
        rightGain: int = max(self.max_gain(root.right), 0)
        sum: int = root.val + leftGain + rightGain
        self.max_sum = max(self.max_sum, sum)
        return root.val + max(leftGain, rightGain)
        

def buildTree(val: int) -> TreeNode :
    root = TreeNode
    if val == 1:
        root.val = 1
        root.left = TreeNode(2)
        root.right=TreeNode(3)
    elif val == 2:
        root.val = -10
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
    return root

thing = Solution()
print(thing.maxPathSum(buildTree(1)))
print(thing.maxPathSum(buildTree(2)))

