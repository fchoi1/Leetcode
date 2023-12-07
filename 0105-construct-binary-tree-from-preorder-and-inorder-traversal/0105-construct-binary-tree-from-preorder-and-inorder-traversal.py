# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        inOrderIndex = 0
        for val in preorder[1:]:
            node = stack[-1]
            if node.val == inorder[inOrderIndex]:
                while stack and stack[-1].val == inorder[inOrderIndex]:
                    node = stack.pop()
                    inOrderIndex+=1
        
                newNode = TreeNode(val)
                node.right = newNode
            else:
                newNode = TreeNode(val)
                node.left = newNode
            stack.append(newNode)

            
        return root
            
        