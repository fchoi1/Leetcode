class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ignore = set()
        runningSum = 0
        node = head
        seen = {0:node}
        while node:
            runningSum += node.val
            if runningSum in seen:
                if runningSum == 0:
                    ignore.add(seen[runningSum])
                if runningSum == 0 or seen[runningSum].next not in ignore:
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
            newnode.next = node
            node = node.next
            newnode = newnode.next
        if newnode:
            newnode.next = None
        return newhead.next
