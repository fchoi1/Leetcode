# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = currNode = head
        while currNode:
            if temp.val != currNode.val:
                temp.next = currNode
                temp = currNode
            currNode = currNode.next
        if temp:
            temp.next = None
        return head
        