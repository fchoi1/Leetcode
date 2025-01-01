# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        ans = []
        if not root:
            return ans
        while q:
            temp = []
            currMax = -inf
            for n in q:
                currMax = max(currMax, n.val)
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            ans.append(currMax)
            q = temp
        
        return ans 
        

        