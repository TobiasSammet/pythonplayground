# You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

# Example 1:
# Input: nums = [1,2,3], head = [1,2,3,4,5]
# Output: [4,5]
# Explanation:
# Remove the nodes with values 1, 2, and 3.

# Example 2:
# Input: nums = [1], head = [1,2,1,2,1,2]
# Output: [2,2,2]
# Explanation:
# Remove the nodes with value 1.

# Example 3:
# Input: nums = [5], head = [1,2,3,4]
# Output: [1,2,3,4]
# Explanation:
# No node has value 5.

# Constraints:

#     1 <= nums.length <= 105
#     1 <= nums[i] <= 105
#     All elements in nums are unique.
#     The number of nodes in the given list is in the range [1, 105].
#     1 <= Node.val <= 105
#     The input is generated such that there is at least one node in the linked list that has a value not present in nums.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
from typing import Optional

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        toRemove = set()
        for num in nums:
            toRemove.add(num)
        #Figure out the head element -- skipping until get valid result
        newHead = head
        while(newHead):
            if newHead.val in toRemove:
                newHead = newHead.next
            else:
                break

        # figure out the rest
        temp = newHead
        while(temp):
            if temp.next == None:
                break
            if temp.next.val in toRemove:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return newHead
    
    def buildList(self, nums: List[int]) -> Optional[ListNode]:
        if len(nums) == 0:
            return None
        
        head = ListNode(nums[0])
        temp = head
        for i in range(1, len(nums)):
            temp.next = ListNode(nums[i])
            temp = temp.next

        return head
    
    def printList(self, head: ListNode) :
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.next

def main(): 
    thingy = Solution()

    thingy.printList(thingy.modifiedList([1,2,3], thingy.buildList([1,2,3,4,5])))
    thingy.printList(thingy.modifiedList([1], thingy.buildList([1,2,1,2,1])))
    
if __name__ == "__main__":
    main()    