from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        theNodes: List[ListNode] = []
        if head == None or head.next == None:
            return
        current: ListNode = head
        while current != None:
            theNodes.append(current)
            current = current.next
        size: int = len(theNodes)
        starter: int = 1
        ender = size -1
        current = head
        while starter <= ender :
            print(ender)
            current.next = theNodes[ender]
            current = current.next
            current.next = theNodes[starter]
            current = current.next
            current.next = None
            starter += 1
            ender -= 1

        head = current

        

def buildList() -> ListNode :
    head: ListNode  = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    return head

def printList(head: ListNode) :
    retVal: str = ""
    temp: ListNode = head
    while temp != None:
        retVal += str(temp.val) + " -> "
        temp = temp.next
    print(retVal)

thing = Solution()
myList = buildList()
printList(myList)
thing.reorderList(myList)
printList(myList)