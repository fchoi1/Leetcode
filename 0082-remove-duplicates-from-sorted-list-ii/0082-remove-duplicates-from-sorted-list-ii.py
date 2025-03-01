# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = head
        prev = newHead = None

        while node:
            curr = node.next
            print(node.val)
            # get next node to check
            if curr and curr.val == node.val:
                # print("dupe")
                while curr and node.val == curr.val:
                    curr = curr.next
                node = curr
                if prev:
                    prev.next = None
            else:
                # print("no dupe")
                if prev:
                    prev.next = node
                prev = node

                if not newHead:
                    newHead = node
                node = node.next

        return newHead
        