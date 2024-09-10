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

            # update prev
            if prev:
                divisor = gcd(prev.val, curr.val)
                prev.next = ListNode(divisor, curr)
            
            # set prev to curr
            prev = curr
            curr = curr.next
        return head
        