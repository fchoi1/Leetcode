# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # traverse until middle
        self.arr = []
        def traverse(node):
            
            if not node:
                return
            
            traverse(node.left)
            self.arr.append(node.val)
            traverse(node.right)
        
        traverse(root)


        def buildTree(arr, parent, isLeft):
            if not arr:
                return parent
            mid = len(arr) // 2

            node = TreeNode(arr[mid])
            if parent:
                if isLeft:
                    parent.left = node
                else:
                    parent.right = node

            left = arr[:mid]
            right = arr[mid + 1:]
            buildTree(left, node, True)
            buildTree(right, node, False)
            return node


        root = buildTree(self.arr, None, None)

        return root