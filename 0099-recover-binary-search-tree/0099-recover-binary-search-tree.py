class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None: 
        self.prev = None
        self.error = None
        self.swapped = False
        def dfs(node):
            if not node or self.swapped:
                return
            dfs(node.left)
            # one swap
            if not self.swapped and self.prev:
                if not self.error and node.val < self.prev.val:
                    self.error = self.prev
                elif self.error and self.error.val < node.val:
                    # swap error node and found prev node
                    self.error.val, self.prev.val = self.prev.val, self.error.val
                    self.swapped = True
            self.prev = node
            dfs(node.right)
        dfs(root)
        
        if not self.swapped:
            self.prev.val, self.error.val = self.error.val, self.prev.val, 
    