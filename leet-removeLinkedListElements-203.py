# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if (head == None):
            return head
        while head != None and head.val == val :
            head = head.next
        if (head == None):
            return head
        last: ListNode = head
        current: ListNode = head.next
        while current != None :
            if current.val == val :
                last.next = current.next
            else :
                last = current
            current = current.next
        return head

def buildList() -> ListNode:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    return head

def printList(head: ListNode):
    retVal: str = ""
    while head != None:
        retVal += str(head.val) + " -> "
        head = head.next
    print(retVal)

thing = Solution()
list = buildList()
printList(list)
newList: ListNode = thing.removeElements(list, 4)
printList(newList)