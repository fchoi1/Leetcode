# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        
        def traverse(node, d):
            if not node or d > depth:
                return

            if d == depth:
                newLeft = TreeNode(val)
                newRight = TreeNode(val)
                newLeft.left, node.left = node.left, newLeft
                newRight.right, node.right = node.right, newRight
                return
            traverse(node.left, d+1)
            traverse(node.right, d+1)
            
        traverse(root, 2)
        return root