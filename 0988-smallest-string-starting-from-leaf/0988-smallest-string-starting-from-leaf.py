# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.smallest = None
        
        def traverse(node, string):
            if not node:
                return
            string = chr(node.val + ord('a')) + string
            if not node.left and not node.right:
                if not self.smallest:
                    self.smallest = string
                else:
                    self.smallest = min(self.smallest, string)
                return
            traverse(node.left, string)
            traverse(node.right, string)

        traverse(root, '')
        return self.smallest
        