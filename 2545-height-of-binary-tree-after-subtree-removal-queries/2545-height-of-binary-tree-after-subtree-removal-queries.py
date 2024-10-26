# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """

        cache = defaultdict(int)
        def dfsLeft(node, level):
            if not node:
                return level            
            cache[node.val] = max(self.maxheight, cache[node.val]) 
            self.maxheight = max(self.maxheight, level)
            l = dfsLeft(node.left, level + 1)
            r = dfsLeft(node.right, level + 1)
   
            return cache[node.val]
        
        def dfsRight(node, level):
            if not node:
                return level            
            cache[node.val] = max(self.maxheight, cache[node.val]) 
            self.maxheight = max(self.maxheight, level)
            r = dfsRight(node.right, level + 1)
            l = dfsRight(node.left, level + 1)
   
            return cache[node.val]
        self.maxheight = 0

        dfsLeft(root,0)
        self.maxheight = 0
        dfsRight(root, 0)
        return [cache[q] for q in queries]

        