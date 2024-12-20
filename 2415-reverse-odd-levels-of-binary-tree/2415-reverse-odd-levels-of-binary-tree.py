# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = [root]
        values = [root.val]
        level = 0
        while q:
            tempQ = []
            tempVal = []
            if level % 2 == 1:
                values.reverse()

            for node, value in zip(q, values):
                node.val = value

                if node.left:
                    tempQ.append(node.left)
                    tempVal.append(node.left.val)
                if node.right:
                    tempQ.append(node.right)
                    tempVal.append(node.right.val)
            q = tempQ
            values = tempVal
            level += 1
            
        return root