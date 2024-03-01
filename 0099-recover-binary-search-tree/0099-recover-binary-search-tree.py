# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # travense in order
        # there should be 2 nodes in wrong order (unless at start or end)
        # check prev 
        self.prev = None
        self.error = None
        self.swapped = False
        def dfs(node):
            if not node or self.swapped:
                return
            dfs(node.left)
            # one swap
            if not self.swapped:
                if not self.error and self.prev and node.val < self.prev.val:
                    self.error = self.prev
                if self.error and self.error.val < node.val:
                    self.error.val, self.prev.val = self.prev.val, self.error.val
                    self.swapped = True
            self.prev = node
            dfs(node.right)
        dfs(root)
        if not self.swapped:
            self.prev.val, self.error.val = self.error.val, self.prev.val, 
    