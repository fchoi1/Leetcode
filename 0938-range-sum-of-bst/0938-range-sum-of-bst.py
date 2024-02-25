class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node, total):
            if not node:
                return total
            if low <= node.val <= high:
                total += node.val
            total = dfs(node.left, total)
            return  dfs(node.right, total)
        return dfs(root, 0)
        