# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.val = root.val
        self.unique = True
        def dfs(node):
            if not node or not self.unique:
                return
            if node.val != self.val:
                self.unique = False
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.unique