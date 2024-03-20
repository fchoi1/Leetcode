# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1
        nodeA = nodeB = None
        i = 0
        # Find A and B
        while node:
            if i + 1 == a:
                nodeA = node
            if i == b:
                nodeB = node.next
                break
            i += 1
            node = node.next
        
        # Get End of List2
        node = list2
        while node.next:
            node = node.next
        
        # Merge
        nodeA.next = list2
        node.next = nodeB

        return list1
        