"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node, res):
            if not node:
                return res
            for child in node.children:
                res = dfs(child,res)
            res.append(node.val)
            return res
        return dfs(root,[])
        