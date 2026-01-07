# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # need the closest 2 sums
        
        @cache
        def getTotal(node):
            if not node:
                return 0            

            return node.val + getTotal(node.left) + getTotal(node.right)
            
        
        total = getTotal(root)
        mod = 10 ** 9 + 7

        self.maxProduct = 1
        def checkSplit(node):
            if not node:
                return

            leftSum = getTotal(node.left)
            rightSum = getTotal(node.right)


            leftHalf = total - leftSum
            rightHalf = total - rightSum

            self.maxProduct = max(self.maxProduct , (leftSum * leftHalf), (rightSum * rightHalf)) 
            checkSplit(node.left)
            checkSplit(node.right)
        
        checkSplit(root)
        return self.maxProduct % mod