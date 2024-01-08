# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def checkNode(node, temp,gap, width):
            if node:
                width = 0 if len(temp) == 0 else width + gap
                if len(temp) != 0:
                    temp.append(gap)   
                temp.append(node)
                width += 1
                return  0, width
            else:
                return gap + 1, width
            

        maxWidth = 1
        q = [root]
        while q:
            temp = []
            currGap = 0
            width = 0
            for node in q:
                if isinstance(node, int):
                    currGap += node * 2
                    continue
                currGap, width = checkNode(node.left, temp, currGap,  width)
                currGap, width = checkNode(node.right, temp, currGap,  width)
            maxWidth = max(width, maxWidth)
            q = temp
        return maxWidth