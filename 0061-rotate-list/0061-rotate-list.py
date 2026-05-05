# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head
        
        l = 1 
        end = head
        while end.next:
            end = end.next
            l += 1
        
        n = (k % l)

        curr = head
        # print(n)
        for _ in range(n):
            curr = curr.next
        
        if not curr.next:
            return head
            
        newHead = curr.next
        curr.next = None
        end.next = head
        return newHead