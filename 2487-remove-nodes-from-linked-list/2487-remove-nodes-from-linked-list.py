# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # strictly decreaseing

        # revese for strictly increase
        # reverse again

        def reverse(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev, node = node, temp
            return prev
        
        curr = last = reverse(head)
        currMax = last.val
        prev = None
        while curr:
            if curr.val >= currMax:
                currMax = curr.val
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next

        return reverse(last)
