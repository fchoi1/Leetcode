# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def dfs(node, res):
            if not node:
                return res
            res.append(node.val)
            res = dfs(node.left, res)
            res = dfs(node.right, res)
            return res
        return dfs(root, [])
        