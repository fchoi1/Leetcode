# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        childs = {}

        for p, c, isLeft in descriptions:
            
            if p not in nodes:
                nodes[p] = TreeNode(p)

            if c not in nodes:
                nodes[c] = TreeNode(c)

            childs[c] = nodes[p]

            if isLeft:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
  
        while c in childs:
            c = childs[c].val
        return nodes[c]
        