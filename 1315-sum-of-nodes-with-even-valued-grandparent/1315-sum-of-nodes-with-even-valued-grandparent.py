class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        self.sum = 0
        def traverse(node, parent, grandparent):
            if not node:
                return
            if grandparent and grandparent.val % 2 == 0:
                self.sum += node.val

            traverse(node.left, node, parent)
            traverse(node.right, node, parent)

        traverse(root, None, None)
        return self.sum