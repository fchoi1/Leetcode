# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs 2 passes?
        q = [(root, 0)]
        
        while q:
            temp = []
            currSum = 0
            nodeVals = []
            prev = None
            
            for i, (node, index) in enumerate(q):

                if node.left:
                    temp.append((node.left, i))
                if node.right:
                    temp.append((node.right, i))

                if prev and prev[1] == index:
                    added = nodeVals[-1] + node.val
                    nodeVals[-1] = added
                    nodeVals.append(added) 
                else:
                    nodeVals.append(node.val)
                currSum += node.val
                prev = (node, index)

            for (node, _), vals in zip(q, nodeVals):
                node.val = currSum - vals

            q = temp

        return root
        