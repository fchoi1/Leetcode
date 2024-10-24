# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 and not root2:
                return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        def dfs(nodeA, nodeB):
            if not nodeA and not nodeB:
                return True
            if not nodeA or not nodeB:
                return False
            
            leftA = nodeA.left.val if nodeA.left else None
            leftB = nodeB.left.val if nodeB.left else None
            rightA = nodeA.right.val if nodeA.right else None
            rightB = nodeB.right.val if nodeB.right else None

            if leftA == leftB and rightA == rightB:
                return dfs(nodeA.left, nodeB.left) and dfs(nodeA.right, nodeB.right)
            elif leftA == rightB and rightA == leftB:
                return dfs(nodeA.left, nodeB.right) and dfs(nodeA.right, nodeB.left)

            return False
                
        return dfs(root1, root2)