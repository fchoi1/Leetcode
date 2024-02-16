class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead = None        
        def reverse(head):
            nonlocal newHead
            count = 0
            node = head
            while count < k and head:
                head = head.next
                count += 1
            if count < k:
                return node, None
            prev = None
            for _ in range(k):
                temp = node.next   
                node.next = prev  
                prev = node      
                node = temp       
            if not newHead:
                newHead = prev
            return prev, node

        node = head
        prev = None
        while node:
            prevNode, nextNode = reverse(node)  
            if prev:
                prev.next = prevNode    
            prev = node                  
            node = nextNode                   
        return newHead if newHead else head