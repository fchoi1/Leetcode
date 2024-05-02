# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.valid = []

        def traverse(node, currSum, path):
            if not node or currSum > targetSum:
                return
            
            path.append(node.val)

            if not node.left and not node.right:
                if currSum + node.val == targetSum:
                    self.valid.append(path.copy())
                if path:
                    path.pop()
                return

            traverse(node.left, currSum + node.val, path)
            traverse(node.right, currSum + node.val, path)
            if path:
                path.pop()
        traverse(root, 0, [])
        return self.valid