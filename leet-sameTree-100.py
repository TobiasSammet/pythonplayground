class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None :
            return True
        if p is None or q is None: 
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def buildTree1() -> TreeNode:
    retVal = TreeNode(1)
    retVal.left = TreeNode(2)
    retVal.right = TreeNode(3)
    return retVal


thing = Solution()

myTree: TreeNode = buildTree1()
myAltTree : TreeNode = buildTree1()
print(thing.isSameTree(myTree, myAltTree))
myAltTree.left.left = TreeNode(4)
print(thing.isSameTree(myTree, myAltTree))