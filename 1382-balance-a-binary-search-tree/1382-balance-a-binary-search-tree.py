# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        # get median

        self.arr = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            self.arr.append(node.val)
            traverse(node.right)

        def createBST(arr):
            if not arr:
                return None
    
            mid = len(arr) // 2
            val = arr[mid]
            node = TreeNode(val)
            if len(arr) == 1:
                return node
            node.left = createBST(arr[:mid])
            node.right = createBST(arr[mid+1:])
            return node

        traverse(root)
        newRoot = createBST(self.arr)
        return newRoot


        