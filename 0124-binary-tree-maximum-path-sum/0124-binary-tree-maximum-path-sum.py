# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        globalMax = root.val 

        def getMax(node):
            nonlocal globalMax
            if not node:
                return 0

            leftSum = max(0, getMax(node.left))
            rightSum = max(0, getMax(node.right))
            theMax = (rightSum + node.val + leftSum)
            globalMax = max(globalMax, theMax)
            return max(leftSum + node.val, rightSum + node.val) 

        getMax(root)
        return globalMax


        # ##  get max left and max right

        # # max sum is max(left) + max(right)
        # ## node next will  be  eitther left or right 
        # return total
        