from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        retVal: List[int] = []
        currentList1 = list1
        currentList2 = list2

        while currentList1 != None or currentList2 != None:
            if currentList1 == None:
                retVal.append(currentList2.val)
                currentList2 = currentList2.next
            elif currentList2 == None:
                retVal.append(currentList1.val)
                currentList1 = currentList1.next
            elif currentList1.val <= currentList2.val:
                retVal.append(currentList1.val)
                currentList1 = currentList1.next
            else:
                retVal.append(currentList2.val)
                currentList2 = currentList2.next
        return self.createListFromArray(retVal)

    
    def createListFromArray(self, nums: List[int]) -> Optional[ListNode]:
        if len(nums) == 0:
            return None
        head: ListNode = ListNode(nums[0])
        temp: ListNode = head
        for i in range(1, len(nums)):
            temp.next = ListNode(nums[i])
            temp = temp.next
        return head

    def printList(self, head: ListNode):
        retVal: str = ""
        temp = head
        while temp != None:
            retVal += f"{temp.val} "
            temp = temp.next
        print(retVal)



thingy = Solution()

# thingy.printList(thingy.createListFromArray([1,2,4]))
thingy.printList(thingy.mergeTwoLists(
    thingy.createListFromArray([1,2,4]),
    thingy.createListFromArray([1,3,4])
))