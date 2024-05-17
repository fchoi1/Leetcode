class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def traverse(node, parent):
            if not node:
                return False
            traverse(node.left, node)
            traverse(node.right, node)
            
            if not node.left and not node.right and parent:
                if node.val == target:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                    return True
                return False
            
        traverse(root,None)
        
        if not root.left and not root.right and root.val == target:
            return None

        return root
        