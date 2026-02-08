# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        nodeBalanced = abs(self.maxDepth(root.left) - self.maxDepth(root.right)) < 2
        
        if nodeBalanced:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
    def maxDepth(self, root):
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        