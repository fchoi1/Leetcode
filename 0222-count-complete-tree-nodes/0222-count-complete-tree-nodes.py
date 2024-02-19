# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # check right and left most
        node = root
        left = right = 0
        while node:
            node = node.left
            left += 1
        node = root
        while node:
            node = node.right
            right += 1
        if left == right:
            return 2 ** left - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        