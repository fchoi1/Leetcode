
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def getTotal(node):
            if not node:
                return
            self.total += node.val
            getTotal(node.left)
            getTotal(node.right)
        getTotal(root)

        def getSum(node, currVal):
            if not node:
                return currVal
            currVal += node.val
            left = getSum(node.left, 0)
            right = getSum(node.right, 0)
            self.product = max(self.product, left *(self.total - left), right *(self.total - right))
            return left + right + currVal
        
        self.product = 1
        getSum(root,0)
        return self.product  % (10 ** 9 + 7)