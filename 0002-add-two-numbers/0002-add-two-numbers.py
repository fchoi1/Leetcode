# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        root = node = ListNode()
        carryOver = 0
        while l1 or l2:
            
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val

            val = val1 + val2 + carryOver
            # print('adding val', val, carryOver)

            if val > 9:
                carryOver = val // 10
                val = val % 10
            else:
                carryOver = 0
            newNode = ListNode(val)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            node.next = newNode
            node = newNode
        
        if carryOver:
            newNode = ListNode(carryOver)
            node.next = newNode

        return root.next