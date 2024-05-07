class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            prev = None
            while node:
                node.next, node, prev = prev, node.next, node
            return prev

        node = start = reverse(head)
        carry = 0
        prev = None
        while node:
            val = node.val * 2 + carry
            node.val = val % 10
            carry = val // 10
            prev = node
            node = node.next

        if carry:
            prev.next = ListNode(carry)
            prev = prev.next
        new = reverse(prev)
        return reverse(start)

