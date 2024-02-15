# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs

        q = [root]
        res = []
        reverse = True
        while q:
            vals = []
            temp = []
            for node in q:
                if not node:
                    continue
                vals.append(node.val)
                temp.append(node.left)
                temp.append(node.right)
            reverse = not reverse
            vals = vals if not reverse else vals[::-1]
            q = temp
            res.append(vals)
        return res[:-1]


        