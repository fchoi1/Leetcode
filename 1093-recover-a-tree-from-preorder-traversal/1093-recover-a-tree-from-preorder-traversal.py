# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        N = len(traversal)
        # get root value
        rootStr = ''
        while i < N and traversal[i] != '-':
            rootStr += traversal[i] 
            i += 1
        root = TreeNode(int(rootStr))
        
        
        stack = [root]
        prevDepth = currDepth = 0
        while i < N:
            if traversal[i] =='-':
                currDepth += 1
                i += 1
            else:
                # we see a node
                num = ''
                while i < N and traversal[i] != '-':
                    num += traversal[i]
                    i += 1
                
                val = int(num)
                newNode = TreeNode(val)
                diff = currDepth - prevDepth

                # Add to left child
                if diff >= 1:
                    parent = stack[-1]
                    parent.left = newNode
                
                # Add to right child
                else:
                    for _ in range(abs(diff) + 1):
                        if len(stack) == 1:
                            break
                        stack.pop()
                    
                    parent = stack[-1]
                    parent.right = newNode 
        
                stack.append(newNode)
                prevDepth = currDepth
                currDepth = 0
          
        return root