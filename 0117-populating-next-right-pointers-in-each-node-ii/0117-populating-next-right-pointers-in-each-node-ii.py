

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque([root])        
        while q:
            prev = None
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr:
                    break
                curr.next = prev
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
                prev = curr
        return root