from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution :
    def oddEvenList(self, head: ListNode) -> str :
        if head == None or head.next == None:
            return head
        onOdd: bool = True
        current: ListNode = head
        oddListCurrent: ListNode = None
        evenListCurrent: ListNode = None
        evenListHead: ListNode = None

        while current:
            if onOdd:
                if oddListCurrent == None:
                    oddListCurrent = current
                else:
                    oddListCurrent.next = current
                    oddListCurrent = oddListCurrent.next
            else:
                if evenListCurrent == None:
                    evenListHead = current
                    evenListCurrent = current
                else :
                    evenListCurrent.next = current
                    evenListCurrent = evenListCurrent.next
            onOdd = not onOdd
            current = current.next
        oddListCurrent.next = evenListHead
        evenListCurrent.next = None
        return head


def buildList(values: List[int]) -> ListNode :
    head: ListNode = ListNode(values[0])
    current: ListNode = head
    for i in range(1, len(values)) :
        current.next = ListNode(values[i])
        current = current.next
    return head

def printList(head: ListNode) :
    retVal: str = ''
    temp: ListNode = head
    while temp :
        retVal += str(temp.val) +  ' -> '
        temp = temp.next
    print (retVal)

thing = Solution()
head = buildList([1,2,3,4,5])
printList(head)
printList(thing.oddEvenList(head))