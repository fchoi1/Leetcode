class Node:
    def __init__(self,val):
        self.val = val
        self.neighbors = {}

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secret = set([0, firstPerson])

        def dfs(node, seen):
            if node in seen:
                return
            seen.add(node)
            secret.add(node.val)
            for nextNode in node.neighbors.values():
                if not nextNode in seen:
                    dfs(nextNode, seen)

        def addSecret(sameTime):
            nodes = {}
            for x, y in sameTime:
                if x not in nodes:
                    nodes[x] = Node(x)
                if y not in nodes:
                    nodes[y] = Node(y)
                nodes[x].neighbors[y] = nodes[y]
                nodes[y].neighbors[x] = nodes[x]

            seen = set()
            for x,y in sameTime:
                if x in seen or y in seen:
                    continue
                if (x in secret or y in secret):
                    dfs(nodes[x], seen)
                
        meetings.sort(key=lambda x: (x[2]))
        prev = meetings[0]
        sameTime = [[prev[0], prev[1]]]
        for x, y, time in meetings[1:]:
            if time == prev[2]:
                sameTime.append([x, y])
            else:
                addSecret(sameTime)
                prev = [x,y,time]
                sameTime = [[x,y]]
        addSecret(sameTime)
        return list(secret)

        