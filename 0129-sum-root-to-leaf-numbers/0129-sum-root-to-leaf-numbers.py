# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # backtrack? 
        # dp?
        self.sum = 0
        def dfs(node, strNum):
            if not node.left and not node.right:
                self.sum += int(strNum + str(node.val))
                return

            if node.left:
                dfs(node.left, strNum + str(node.val))
            
            if node.right:
                dfs(node.right, strNum + str(node.val))

        dfs(root, '')
        return self.sum
        