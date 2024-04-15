# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.sum = 0
        def traverse(node, path):
            if not node:
                return
            curr = path * 10 + node.val
            if not node.left and not node.right:
                self.sum += curr
            traverse(node.left, curr)
            traverse(node.right, curr)
            

        traverse(root, 0)

        return self.sum
