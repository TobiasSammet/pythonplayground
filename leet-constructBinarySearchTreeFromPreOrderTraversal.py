from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return
        root: TreeNode = TreeNode(preorder[0])            
        for i in range(1, len(preorder)) :
            temp: TreeNode = root
            while True:
                if preorder[i] < temp.val :
                    if temp.left is None :
                        temp.left = TreeNode(preorder[i])
                        break
                    else :
                        temp = temp.left
                else :
                    if temp.right is None :
                        temp.right = TreeNode(preorder[i])
                        break
                    else :
                        temp = temp.right
        return root

def printTree(root: TreeNode, location: str) :
    if root is None: 
        return
    print(location + " " + str(root.val))
    printTree(root.left, location + " -> left")
    printTree(root.right, location + " -> right")


thing = Solution()

preorder: List[int] = [8,5,1,7,10,12]

root = thing.bstFromPreorder(preorder)
printTree(root, "root")

print(thing.bstFromPreorder(preorder))