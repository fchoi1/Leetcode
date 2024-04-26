
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.product = 1

        def getSum(node, currVal):
            if not node:
                return currVal
            currVal += node.val
            left = getSum(node.left, 0)
            right = getSum(node.right, 0)
            self.product = max(self.product, left *(self.total - left), right *(self.total - right))
            return left + right + currVal
            
        self.total = getSum(root,0)
        self.product = 1
        getSum(root,0)
        return self.product  % (10 ** 9 + 7)