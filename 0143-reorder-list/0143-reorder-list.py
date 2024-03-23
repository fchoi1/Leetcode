class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = slow.next
        slow.next = prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        l1 = head
        l2 = prev

        while l1 and l2:
            temp = l1.next
            temp2 = l2.next
            l1.next = l2
            l1.next.next = temp

            l2 = temp2
            l1 = temp

        return head