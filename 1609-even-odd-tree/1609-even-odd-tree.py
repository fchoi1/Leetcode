class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        steps = 0
        while q:
            prev = -inf if steps % 2 == 0 else inf
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if (steps % 2 == 0 and (prev >= curr.val or curr.val % 2 == 0)) or \
                    (steps % 2 == 1  and (prev <= curr.val or curr.val % 2 == 1)):
                    return False
                prev = curr.val
            steps += 1
        return True