class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # in order traversal
        self.maxCount = 0
        self.prev = None
        self.res = set()
        def dfs(node, count):
            if not node:
                return count
            count = dfs(node.left, count)

            count = 1 if not self.prev or self.prev.val != node.val else count + 1

            if count > self.maxCount:
                self.maxCount = count
                self.res = set([node.val])
            elif count == self.maxCount:
                self.res.add(node.val)

            self.prev = node
            count = dfs(node.right, count)
            return count
        dfs(root, 1)
        return list(self.res)
