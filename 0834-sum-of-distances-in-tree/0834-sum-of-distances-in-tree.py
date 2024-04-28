class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjMap = defaultdict(set)
        for a, b in edges:
            adjMap[a].add(b)
            adjMap[b].add(a)

        seen = set()
        ans = [0 for _ in range(n)]
        memo = [None for _ in range(n)]
        def getDist(node):
            seen.add(node)
            totalDist = nodeCount = 0
            for nextNode in adjMap[node]:
                if nextNode in seen:
                    continue
                nodeDist, count = getDist(nextNode)
                totalDist += nodeDist
                nodeCount += count
            memo[node] = nodeCount + 1 
            return totalDist + nodeCount, nodeCount + 1

        ans[0] = getDist(0)[0]
        seen = set()
        def traverse(node, prev):
            seen.add(node)
            if prev != None:
                ans[node] = ans[prev] + n - memo[node] * 2
            for nextNode in adjMap[node]:
                if nextNode in seen:
                    continue
                traverse(nextNode, node)
        traverse(0, None)
        return ans