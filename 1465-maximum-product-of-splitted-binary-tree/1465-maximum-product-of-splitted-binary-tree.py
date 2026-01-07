# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # need the closest 2 sums
        cache = defaultdict(int)

        def getTotal(node):
            if cache[node]:
                return cache[node]

            if not node:
                return 0            
            cache[node] = node.val + getTotal(node.left) + getTotal(node.right)
            
            return cache[node] 
            
        
        total = getTotal(root)
        mod = 10 ** 9 + 7

        maxProduct = 1

        for val in cache.values():
            maxProduct = max(maxProduct, (total - val) * val)
            
        return maxProduct % mod