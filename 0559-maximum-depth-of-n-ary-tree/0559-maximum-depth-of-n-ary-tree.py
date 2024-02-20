"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.depth = 0
        def dfs(node, level):
            if not node.children:
                self.depth = max(self.depth, level)
                return
            for child in node.children:
                dfs(child, level+1)
        dfs(root, 1)
        return self.depth