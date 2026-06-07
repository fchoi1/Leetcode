# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        r = {} # to find root
        nodes = set()
        c_set = set()


        for p, c, isLeft in descriptions:
            


            child = TreeNode(c) if c not in r else r[c]
            parent = TreeNode(p) if p not in r else r[p]
            r[p] = parent
            r[c] = child

            if isLeft:
                parent.left = child
            else:
                parent.right = child
            
            if parent not in c_set:
                nodes.add(parent)
            nodes.discard(child)
            c_set.add(child)


        root = nodes.pop()
        return root