class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        prevLeft = leftNode = rightNode = None
        i = 1
        while node:
            if left > 1 and i == (left - 1):
                prevLeft = node
            if i == left:
                leftNode = node
            if i == right:
                rightNode = node
                break
            node = node.next
            i += 1
            
        # reverse
        prev = end = rightNode.next
        while leftNode != end:
            temp = leftNode.next
            leftNode.next = prev
            prev = leftNode
            leftNode = temp

        if prevLeft:
            prevLeft.next = prev
        return head if left != 1 else prev


        
        