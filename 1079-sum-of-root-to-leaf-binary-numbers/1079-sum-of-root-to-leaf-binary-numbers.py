# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.sum = 0


        def dfs(node, binStr):
            binStr += str(node.val)
            if not node.right and not node.left:
                self.sum += int(binStr, 2)
                return
            
            if node.right:
                dfs(node.right, binStr)
            
            if node.left:
                dfs(node.left, binStr)

        dfs(root, '')

        return self.sum