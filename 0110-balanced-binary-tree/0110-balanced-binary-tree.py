# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        self.isBalanced = True
        @cache
        def checkDepth(node):
            if not node:
                return 0
            left = checkDepth(node.left)
            right = checkDepth(node.right)

            if abs(right - left) > 1:
                self.isBalanced = False

            return 1 + max(left, right)
        
        checkDepth(root)

        return self.isBalanced
            

        