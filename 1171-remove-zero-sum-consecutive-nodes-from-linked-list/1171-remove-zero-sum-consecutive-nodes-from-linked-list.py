# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {0: head}
        ignore = set()
        runningSum = 0
        node = head
        # for i, val in enumerate(arr):
        while node:
            runningSum += node.val
            if runningSum == 0:
                ignore.add(seen[runningSum])
            if runningSum in seen:
                if seen[runningSum].next not in ignore:
                    while seen[runningSum] != node:
                        seen[runningSum] = seen[runningSum].next
                        ignore.add(seen[runningSum])
            seen[runningSum] = node
            node = node.next

        newnode = newhead = ListNode()
        node = head
        i = 0
        while node:
            if node in ignore:
                # i += 1
                node = node.next
                continue
            newnode.next = ListNode(node.val)
            # i += 1
            node = node.next
            newnode = newnode.next
        return newhead.next
