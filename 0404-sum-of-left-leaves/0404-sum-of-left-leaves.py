class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.leftSum = 0

        def traverse(node, isLeft):
            if not node:
                return
            
            if isLeft and not node.left and not node.right:
                self.leftSum += node.val
                return
            
            traverse(node.left, True)
            traverse(node.right, False)
        traverse(root, False)

        return self.leftSum