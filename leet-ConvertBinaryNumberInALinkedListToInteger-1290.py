from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if head == None:
            return 0
        retVal: int = 0
        currentNode = head
        while currentNode != None:
            retVal = (retVal * 2) + currentNode.val
            currentNode = currentNode.next

        return retVal
    
thingy = Solution()
print(thingy.getDecimalValue(ListNode(1)))

node1 = ListNode(1)
node1.next = ListNode(0)
node1.next.next = ListNode(1)
print(thingy.getDecimalValue(node1))


