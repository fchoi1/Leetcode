# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # root, left, right
        node = root
        # store right node
        # set root right to left, then set the chhild of right to temp

        def dfs(node):
            if not node:
                return
            temp = None
            if node.right:
                temp = node.right
                dfs(node.right)

            if node.left:
                node.right = node.left
                dfs(node.left)
                node.left = None
                while node.right:
                    node = node.right
                node.right = temp
        dfs(root)
        