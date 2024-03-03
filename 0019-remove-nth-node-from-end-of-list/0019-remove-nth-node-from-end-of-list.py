# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        target = length - n
        if target == 0:
            return head.next
        node = head
        while target > 1:
            target -= 1
            node = node.next
        node.next = node.next.next
        return head
        