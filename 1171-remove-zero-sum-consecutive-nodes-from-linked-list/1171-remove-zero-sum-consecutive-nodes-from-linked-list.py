# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        seen = {}
        ignore = set()
        runningSum = 0
        for i, val in enumerate(arr):
            runningSum += val
            if runningSum == 0:
                ignore.update(range(i+1))
            else:
                if runningSum in seen:
                    if seen[runningSum] + 1 not in ignore:
                        ignore.update(range(seen[runningSum]+1, i+1))
            seen[runningSum] = i
        print(ignore)
        node = newhead = ListNode()
        for i, val in enumerate(arr):
            if i in ignore:
                continue
            node.next = ListNode(val)
            node = node.next
        return newhead.next
# 2 1 1 1 -4 3 1
# 2 3 4 5. 1 4 5

# 1 3 2 -3 -2 5 5 -5 1
# 1 4 6 3  1  6 11 6 1

# 1 2 -3 3 1
# 1 3 0 3 4