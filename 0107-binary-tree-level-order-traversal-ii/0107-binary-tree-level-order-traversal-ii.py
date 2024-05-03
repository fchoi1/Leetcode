class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs
        if not root:
            return []
        q = deque([root])
        level = []
        while q:
            row = []
            for _ in range(len(q)):
                
                node = q.popleft()
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level.append(row)
        return level[::-1]
        