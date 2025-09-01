# Definition for a binary tree node.
COUNT: int = 10

class TreeNode:
    val: int =0
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root  :
            return None
        if root.val == val :
            return root
        if root.val > val :
            return self.searchBST(root.left, val)
        else :
            return self.searchBST(root.right, val)


def constructTree() :
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)

    return root

def print2DUtil(root: TreeNode, space: int):
    if root == None:
        return
    space += COUNT
    print2DUtil(root.right, space)
    print('')
    spaces: str = ''
    for i in range(COUNT, space):
        spaces += ' '
    print(spaces + str(root.val))        
    print2DUtil(root.left, space)
    

def print2D(root: TreeNode):
    print2DUtil(root, 0)


thing = Solution()
root = constructTree()
print2D(thing.searchBST(root, 2))
