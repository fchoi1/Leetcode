# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ignore = set()
        runningSum = 0
        node = head
        seen = {0:node}
        while node:
            runningSum += node.val
            # if runningSum ==
            if runningSum in seen:
                if runningSum == 0:
                    print(node, "SEEN", seen[runningSum])
                    ignore.add(seen[runningSum])
                    while seen[runningSum] != node:
                        seen[runningSum] = seen[runningSum].next
                        ignore.add(seen[runningSum])
                elif seen[runningSum].next not in ignore:
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
                node = node.next
                continue
            newnode.next = ListNode(node.val)
            node = node.next
            newnode = newnode.next
        return newhead.next
