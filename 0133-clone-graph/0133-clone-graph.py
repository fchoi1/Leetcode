from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        nodeList = {}
        seen = set()
        start = node.val
        q = deque([node])
        while q:
            node = q.popleft()
            val = node.val
            if val in seen:
                continue
            seen.add(val)
            newNeighbors = []
            for neighbor in node.neighbors:
                if neighbor.val not in nodeList:
                    nodeList[neighbor.val] = Node(neighbor.val)
                newNeighbors.append(nodeList[neighbor.val])
                q.append(neighbor)
            if node.val in nodeList:
                nodeList[val].neighbors = newNeighbors
            else:
                nodeList[val] = Node(val, newNeighbors)
        return nodeList[start]   