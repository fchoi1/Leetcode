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
            currSum = 0
            while curr and curr.val != 0:
                currSum += curr.val
                curr = curr.next
    
            newNode.next = ListNode(currSum)
            newNode = newNode.next
            curr = curr.next
            
        return newHead.next