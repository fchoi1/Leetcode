# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # get deepest

        # for each deepest, we need the path,  after we check and zip until. 
        # dfs

        # dfs to get the deepest, 
        self.depth = 0
        self.lca = None
        def isDeepest(node, d):

            if not node:
                self.depth = max(self.depth, d)
                return d  

            
            left = isDeepest(node.left, d + 1)
            right = isDeepest(node.right, d + 1)
            
            if left == right and left == self.depth:
                self.lca = node
            return max(left, right)

        isDeepest(root,0)
        return self.lca
        