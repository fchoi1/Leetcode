# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        newHead = newNode = ListNode()
        
        while curr:
            while curr and curr.val != 0:
                curr = curr.next
            
            currSum = 0
            while prev != curr:
                currSum += prev.val
                prev = prev.next

            newNode.next = ListNode(currSum)
            newNode = newNode.next
            curr = curr.next
            
        return newHead.next