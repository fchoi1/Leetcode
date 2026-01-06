class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        level = lvl = 1
        q = deque([root])
        while q:
            currSum = 0
            for _ in range(len(q)):
                curr = q.popleft()
                currSum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if currSum > maxSum:
                maxSum = currSum
                level = lvl
            lvl += 1
        return level
        