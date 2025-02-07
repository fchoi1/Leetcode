# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        # sort?
        self.l1 = []
        self.l2 = []

        def traverse(node, list):
            if not node:
                return

            list.append(node.val)
            traverse(node.left, list)
            traverse(node.right, list)

        traverse(root1, self.l1)
        traverse(root2, self.l2)

        return sorted(self.l1 + self.l2)
            
        