# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # get path of start
        # get path of dest
        # get common
        def findNode(curr, node, nodePath, path):
            if not curr:
                return [], ""
            if curr.val == node:
                return nodePath, path

            leftNodePath, leftPath = findNode(curr.left, node, nodePath + [curr.val], path + "L")
            rightNodePath, rightPath = findNode(curr.right, node, nodePath + [curr.val], path + "R")
            if not leftNodePath and rightNodePath:
                return rightNodePath, rightPath
            if not rightNodePath and leftNodePath:
                return leftNodePath, leftPath
            return [], ""
        

        startNodes, startPath = findNode(root, startValue, [], "")
        destNodes, destPath = findNode(root, destValue, [], "")
        start = {x:i+1 for i,x in enumerate(startNodes[::-1])}
        start[startValue] = 0

        # print(startNodes, startPath, start)
        # print(destNodes, destPath)
        path = ""
        N = len(destPath)
        if destValue in start:
            return "U" * start[destValue]

        for i, node in enumerate(destNodes[::-1]):
            if node in start :
                return "U" * start[node] + destPath[N-i-1:]

        return "U" * len(start) + destPath

            
        