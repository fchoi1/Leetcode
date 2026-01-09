# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # get all deepest,
        # get the common ancestor

        
        self.maxDepth = 0
        self.nodes = []
        def getDeepest(node, depth, path):
            
            path.append(node)
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.nodes = [path.copy()]
            elif depth == self.maxDepth:
                self.nodes.append(path.copy())
            
            
            if node.left:
                getDeepest(node.left, depth + 1, path)
            if node.right:
                getDeepest(node.right, depth + 1, path)
            path.pop()
        
        getDeepest(root, 1, [])

        prev = root
        for i in range(self.maxDepth):
            curr = self.nodes[0][i]
            if all(nodeList[i] == curr for nodeList in self.nodes):
                prev = curr 
                continue
            else:
                return prev


        return prev