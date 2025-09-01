# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next == None):
            return head
        newHead = head.next
        rest = newHead.next
        newHead.next = head
        newHead.next.next = self.swapPairs(rest)
        return newHead
    

def printList(head: Optional[ListNode]) -> str:
    if head == None: 
        return ""
    retVal: str = ""
    temp = head
    while(temp):
        retVal += (str(temp.val) + ", ")
        temp = temp.next

    if len(retVal) > 0:
        retVal = retVal[:-2]
    return retVal

def constructList1() -> ListNode:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    return head

def constructList2() -> ListNode:
    head = ListNode(1, ListNode(2, ListNode(3)))
    return head


thingy = Solution()

print(printList(thingy.swapPairs(constructList1())))
print(printList(thingy.swapPairs(constructList2())))