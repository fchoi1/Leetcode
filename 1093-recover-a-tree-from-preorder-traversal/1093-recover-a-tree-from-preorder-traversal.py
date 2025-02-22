# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        d = i = 0
        nodes = [] # (node, depth)
        N = len(traversal)
        while i < N:
            if traversal[i] =='-':
                d += 1
                i += 1
            else:
                num = ''
                while i < N and traversal[i] != '-':
                    num += traversal[i]
                    i += 1
                nodes.append((int(num),d))
                d = 0
        

        root = TreeNode(nodes[0][0])

        stack = [root]
        prevDepth = 0

        for currNode in nodes[1:]:
            val, depth = currNode

            newNode = TreeNode(val)
            diff = depth - prevDepth

            print("d", depth, prevDepth)

            if diff >= 1:
                parent = stack[-1]
                parent.left = newNode
            else:
                for _ in range(abs(diff) + 1):
                    if len(stack) == 1:
                        break
                    stack.pop()
                
                parent = stack[-1]
                parent.right = newNode 
      
            stack.append(newNode)
            prevDepth = depth

        return root