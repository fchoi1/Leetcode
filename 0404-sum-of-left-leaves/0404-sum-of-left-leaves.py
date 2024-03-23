class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def traverse(node, isLeft):
            if not node:
                return 

            if not node.left and not node.right and isLeft:
                self.sum += node.val
                return
            
            traverse(node.left, True)
            traverse(node.right, False)
            
        traverse(root, False)
        return self.sum
        