# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.cache = {}

        def isDeepest(node, d): # returns lca and depth
            if (node, d) in self.cache:
                print("CACACACC")
                return self.cache[(node,d)]

            if not node.left and not node.right:
                return node, d

            left_lca, left_depth = isDeepest(node.left, d + 1) if node.left else (node, d)
            right_lca, right_depth = isDeepest(node.right, d + 1) if node.right else (node, d)
            

            if left_depth == right_depth:
                self.cache[(node,d)] = (node, left_depth)
            else:
                self.cache[(node,d)] = (left_lca, left_depth) if left_depth > right_depth else (right_lca, right_depth)
  
            return self.cache[(node,d)]

        lca, _ = isDeepest(root,0)
        return lca
        