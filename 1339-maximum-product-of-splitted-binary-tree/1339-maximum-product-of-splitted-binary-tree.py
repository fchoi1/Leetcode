
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        self.values = set()
        def getSum(node, currVal):
            if not node:
                return currVal
            currVal += node.val
            left = getSum(node.left, 0)
            right = getSum(node.right, 0)
            self.values.add(left)
            self.values.add(right)
            return left + right + currVal

        total = getSum(root, 0)
        product = 1
        for val in self.values:
            product = max(product, (total - val) * val)
        return product % (10 ** 9 + 7)