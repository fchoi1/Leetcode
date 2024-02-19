# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    
        res = []
        def dfs(node,string):
            if not node:
                return
            nodeStr = f"{string}->{node.val}" if string else str(node.val)
            if not node.left and not node.right:
                res.append(nodeStr)
                return
            dfs(node.left, nodeStr)
            dfs(node.right, nodeStr)
        dfs(root,"")
        return res

        