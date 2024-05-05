# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        prev = None
        while nextNode:
            node.val = nextNode.val
            prev = node
            node = node.next
            nextNode = nextNode.next
        prev.next = None
        
            
            
