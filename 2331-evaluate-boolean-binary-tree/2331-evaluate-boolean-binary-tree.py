class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        

        def traverse(node):
            if not node.left and not node.right:
                return node.val
            
            left = traverse(node.left)
            right = traverse(node.right)
            if node.val == 2:
                return left or right
            else:
                return left and right
        
        return traverse(root)
