# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(node, num):
            if not node:
                return
            new = int(str(num) + str(node.val))
            if not node.left and not node.right:
                self.total += new
                return
                
            dfs(node.left, int(new))
            dfs(node.right, int(new))

        dfs(root, 0)
        return self.total