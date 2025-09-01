from typing import List
import math 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count: int = 0
        temp: ListNode = head
        while(temp) :
            count +=1
            temp = temp.next
        x = math.floor(count / 2) + 1
        print(x)
        temp = head
        for i in range(1, x): 
            temp = temp.next
        return temp


def buildList(values: List[int]) -> ListNode :
    head: ListNode = ListNode(values[0])
    current: ListNode = head
    for i in range(1, len(values)) :
        current.next = ListNode(values[i])
        current = current.next
    return head

def printList(head: ListNode) :
    retVal: str = '';
    temp: ListNode = head
    while temp :
        retVal += str(temp.val) +  ' -> '
        temp = temp.next
    print (retVal)


thing = Solution()
head = buildList([1,2,3,4,5])
printList(head)
printList(thing.middleNode(head))

