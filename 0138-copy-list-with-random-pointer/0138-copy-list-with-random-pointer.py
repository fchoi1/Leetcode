class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(0)
        prev = newHead
        while head:
            newNode = Node(head.val,None,head.random)
            prev.next = newNode
            prev = prev.next
            head.new = newNode
            head = head.next

        node = newHead.next
        while node:
            if node.random:
                node.random = node.random.new
            node = node.next
        return newHead.next
