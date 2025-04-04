# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.depth = 0
        self.lca = None
        self.cache = {}

        def isDeepest(node, d):
            if (node,d) in self.cache:
                return self.cache[(node,d)]

            if not node:
                self.depth = max(self.depth, d)
                return d  

            left = isDeepest(node.left, d + 1)
            right = isDeepest(node.right, d + 1)
            
            if left == right and left == self.depth:
                self.lca = node

            self.cache[(node,d)] = max(left, right)
            return self.cache[(node,d)]

        isDeepest(root,0)
        return self.lca
        