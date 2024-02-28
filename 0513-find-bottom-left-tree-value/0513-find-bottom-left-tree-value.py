class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.depth  = 0
        self.left = root
        def dfs(node, level):
            if not node:
                return
            if level > self.depth:
                self.depth = level
                self.left = node
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return self.left.val
        