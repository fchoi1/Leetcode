# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        binStr = ''
        curr = head
        while curr:
            binStr += str(curr.val)
            curr = curr.next
        
        return int(binStr,2)
        