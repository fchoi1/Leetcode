# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def getSumTilt(node):
            if not node:
                return 0
            leftSum, rightSum = getSumTilt(node.left), getSumTilt(node.right)
            self.total += abs(leftSum - rightSum)
            return leftSum + rightSum + node.val
        getSumTilt(root)
        return self.total