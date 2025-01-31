# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,count):
            if not node:
                return count 
            return dfs(node.right, count) + dfs(node.left, count) + 1
        
        return dfs(root, 0) 