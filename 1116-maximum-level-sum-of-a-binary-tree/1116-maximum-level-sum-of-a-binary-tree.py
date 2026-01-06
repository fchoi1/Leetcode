# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = (-inf, -1) # val, level
        lvl = 0
        q = [root]

        while q:
            temp = []
            levelSum = 0
            for curr in q:
                levelSum += curr.val
                if curr.left:
                    temp.append(curr.left)
                
                if curr.right:
                    temp.append(curr.right)
            lvl += 1
            maxSum = max(maxSum, (levelSum, -lvl))
            q = temp

        return -maxSum[1]