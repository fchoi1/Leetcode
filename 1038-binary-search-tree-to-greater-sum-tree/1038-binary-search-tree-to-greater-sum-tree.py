class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.prefix = []

        def traverse(node):
            if not node:
                return
            traverse(node.right)
            if self.prefix:
                self.prefix.append(self.prefix[-1] + node.val)
            else:
                self.prefix.append(node.val)
            traverse(node.left)

        def update(node):
            if not node:
                return
            update(node.left)
            node.val = self.prefix[self.idx]
            self.idx -= 1
            update(node.right)

        traverse(root)
        self.idx = len(self.prefix) - 1
        update(root)
        return root
