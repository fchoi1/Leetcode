class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        seen = {}
        res = set()
        def generateSubTree(node):
            if not node:
                return None
            inOrder = (generateSubTree(node.left), node.val,generateSubTree(node.right))
            if inOrder in seen:
                res.add(seen[inOrder])
            else:
                seen[inOrder] = node


            return tuple(inOrder)
        generateSubTree(root)
        return res

            
        