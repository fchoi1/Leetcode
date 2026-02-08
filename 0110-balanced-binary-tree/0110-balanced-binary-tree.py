# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        self.isBalanced = True
        def checkDepth(node, depth):
            if not node:
                return depth
            left = checkDepth(node.left, depth + 1)
            right = checkDepth(node.right, depth + 1)

            if abs(right - left) > 1:
                self.isBalanced = False

            return max(left, right)
        
        checkDepth(root, 0)

        return self.isBalanced
            

        