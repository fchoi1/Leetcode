class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            row = []
            for _ in range(len(q)):
                curr = q.popleft()
                row.append(curr.val)
                if curr.children:
                    for child in curr.children:
                        q.append(child)
                     
            res.append(row)
        return res
        