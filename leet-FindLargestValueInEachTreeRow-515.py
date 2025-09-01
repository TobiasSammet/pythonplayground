from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        retVal: List[int] = []
        if not root: 
            return retVal
        retVal.append(root.val)
        level: List[TreeNode] = []
        level.append(root.left)
        level.append(root.right)
        self.processLevel(level, retVal)
        return retVal
    
    def processLevel(self, level: List[TreeNode], biggestValue: List[int]) :
        if not level: 
            return
        # there is a bug right here
        temp: int = -10000
        foundValue: bool = False
        nextLevel: List[TreeNode] = []
        while level:
            current: TreeNode = level.pop(0)
            if current: 
                foundValue = True
                if current.val > temp :
                    temp = current.val
                nextLevel.append(current.left)
                nextLevel.append(current.right)
        if foundValue :
            biggestValue.append(temp)
        self.processLevel(nextLevel, biggestValue)




class Starter:
    def Main(self) :
        print("Hello")
        thing = Solution()
        root: TreeNode = self.buildTree()
        print(thing.largestValues(root))
        

    def buildTree(self) -> TreeNode :
        root: TreeNode = TreeNode(1)
        root.left = TreeNode(3)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(9)
        return root

thing = Starter()
thing.Main()        