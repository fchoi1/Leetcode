class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first = head
        head = head.next
        prev = None
        while first:
            if first.next:
                second = first.next
            else:
                break

            first.next = second.next
            second.next = first
            if prev:
                prev.next = second
            prev = first
            first = first.next
        return head

        