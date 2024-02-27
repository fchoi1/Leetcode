# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def getLongest(node):
            if not node:
                return 0
            left = getLongest(node.left) 
            right = getLongest(node.right)
            self.longest = max(self.longest, left + right + 1 )
            return max(left, right ) + 1
            
        getLongest(root)
        return self.longest - 1