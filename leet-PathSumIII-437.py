# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None :
            return 0
        return self.internalPathSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def internalPathSum(self, root: TreeNode, sum: int) -> int :
        if root == None: 
            return 0
        retVal : int = 0
        if root.val == sum:
            retVal = 1
        return retVal + self.internalPathSum(root.left, sum - root.val) + self.internalPathSum(root.right, sum - root.val)
        
def createTree() -> TreeNode:
    root: TreeNode = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode (11)
    
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    
    
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    return root

thing = Solution()
root = createTree()
print(thing.pathSum(root, 22))