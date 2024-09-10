# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr:
            if prev:
                prev.next = ListNode(gcd(prev.val, curr.val), curr)
            prev = curr
            curr = curr.next
        return head
        