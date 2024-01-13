"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        nodeList = {}
        seen = set()
        start = node.val
        q = [node]
        while q:
            temp = []
            for node in q:
                val = node.val
                if val in seen:
                    continue
                seen.add(val)
                newNeighbors = []
                for neighbor in node.neighbors:
                    if neighbor.val not in nodeList:
                        nodeList[neighbor.val] = Node(neighbor.val)
                    newNeighbors.append(nodeList[neighbor.val])
                    temp.append(neighbor)
                if node.val in nodeList:
                    nodeList[val].neighbors = newNeighbors
                else:
                    nodeList[val] = Node(val, newNeighbors)
            q = temp
        return nodeList[start]   