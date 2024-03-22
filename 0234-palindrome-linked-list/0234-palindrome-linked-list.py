# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # reverse

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        node = slow
        prev = None

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        node = prev

        while head and node:
            if head.val != node.val:
                return False
            head = head.next
            node = node.next

        return True
        
        