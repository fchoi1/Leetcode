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
        
        maxWidth = 1
        q = [(root, 1)]
        while q:
            temp = []
            minStart = float('Inf')
            maxStart = 0
            for node,i in q:
                if node.left:
                    temp.append((node.left, i*2))
                    minStart = min(minStart, i*2)
                    maxStart = max(maxStart, i*2)
                if node.right:
                    temp.append((node.right, i*2 + 1))
                    minStart = min(minStart, i*2+1)
                    maxStart = max(maxStart, i*2+1)
            if maxStart > minStart:
                maxWidth = max(maxWidth, (maxStart - minStart) + 1)
            q = temp
        return maxWidth