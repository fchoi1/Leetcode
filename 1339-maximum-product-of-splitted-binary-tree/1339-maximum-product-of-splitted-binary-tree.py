# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # sum are close to equal
        # 1 2 3 4  5
        # 1 * 14
        # 3 * 12 = 36
        # 6 * 9 = 54
        # 10 * 5 = 50
        # 15
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
            print(node.val, left, right, self.product)
            self.product = max(self.product, left *(self.total - left), right *(self.total - right))
            if left > (10**9 + 7) or right > (10**9 + 7) or self.product > (10**9 + 7):
                print('greater', left, right, self.product)
            # self.product = self.product % (10**9 + 7)
            return left + right + currVal
        
        self.product = 1
        getSum(root,0)
        return self.product  % (10 ** 9 + 7)