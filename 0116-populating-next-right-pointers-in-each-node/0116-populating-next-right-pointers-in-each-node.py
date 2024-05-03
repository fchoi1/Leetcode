"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        # BFS

        q = deque([root])
        
        while q:
            prev = None
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr:
                    break
                curr.next = prev
                q.append(curr.right)
                q.append(curr.left)
                prev = curr
        return root

        