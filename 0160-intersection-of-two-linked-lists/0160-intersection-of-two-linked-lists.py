# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        node = headA
        while node:
            seen.add(node)
            node = node.next
        
        node = headB
        while node:
            if node in seen:
                return node
            node = node.next
        return None