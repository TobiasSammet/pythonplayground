from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        if (node == None):
            return
        if (node.next == None): 
            return
        node.val = node.next.val
        node.next = node.next.next
        
        
def buildList(values: List[int]) -> ListNode:
    if(len(values) == 0):
        return None
    head: ListNode = ListNode(values[0])
    current: ListNode = head
    for i in range(1,len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

def printList(myList: ListNode) :
    retVal: str = ""
    while(myList != None):
        retVal += " " + str(myList.val) + " ->"
        myList = myList.next
    print(retVal)

myList = buildList([1,2,3,4])
printList(myList)
thing = Solution()
thing.deleteNode(myList.next)
printList(myList)