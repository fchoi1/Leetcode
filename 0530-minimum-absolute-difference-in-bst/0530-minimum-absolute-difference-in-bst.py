# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.diff = self.prev = inf
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            self.diff = min(self.diff, abs(self.prev - node.val))
            self.prev = node.val
            dfs(node.right)
        dfs(root)
        return self.diff