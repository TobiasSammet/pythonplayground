from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ElementList: List[int]
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.ElementList = []
        self.TraverseTree(root1)
        self.TraverseTree(root2)
        self.ElementList.sort()
        return self.ElementList

    def TraverseTree(self, root: TreeNode) :
        if root == None:
            return
        self.ElementList.append(root.val)
        self.TraverseTree(root.left)
        self.TraverseTree(root.right)

def BuildTree1():
    root: TreeNode = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    return root

def BuildTree2():
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    return root


thing = Solution()

tree1: TreeNode = BuildTree1()
tree2: TreeNode = BuildTree2()

print(thing.getAllElements(tree1, tree2))    