class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev