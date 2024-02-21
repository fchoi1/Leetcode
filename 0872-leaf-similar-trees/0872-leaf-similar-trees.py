# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getLeafValue(node, arr):
            if not node:
                return arr
            if not node.left and not node.right:
                arr.append(node.val)
            else:
                arr = getLeafValue(node.left, arr)
                arr = getLeafValue(node.right, arr)
            return arr
        left = getLeafValue(root1, [])
        right = getLeafValue(root2, [])
        if len(left) != len(right):
            return False
        for l, r in zip(left, right):
            if l != r:
                return False
        return True
        