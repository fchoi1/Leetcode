# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.valid = []
        def dfs(node, path, currSum):
            if not node:
                return
            if  not node.left and not node.right:
                if targetSum == currSum + node.val:
                    self.valid.append(path + [node.val])
                return

            dfs(node.left, path + [node.val], currSum + node.val)
            dfs(node.right, path + [node.val], currSum + node.val)
        
        dfs(root, [], 0)
        return self.valid
