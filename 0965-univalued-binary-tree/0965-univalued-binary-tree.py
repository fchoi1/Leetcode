class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        
        if root.left and root.val != root.left.val:
            return False

        if root.right and root.val != root.right.val:
            return False
        
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)