class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # 0 1 2 3 3 3 
        # 1 0 1 2 2 2  
        # 2 1 0 1 1 1
        # 3 2 1 0 2 2
        # 3 2 1 2 0 2
        

        #。+ 1 for all next ones
        # -1 for all prev ones
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
                # memomize
            print(node, totalDist + nodeCount, nodeCount)
            memo[node] = (totalDist + nodeCount, nodeCount + 1)
            return totalDist + nodeCount, nodeCount + 1

        ans[0] = getDist(0)[0]
        print(memo)
        # 2: 8 - 4 -3 +  2nodes, + 3 = 6
        # 1: 8  -0 -1 +  5nodes, + 0

        # 3: 6 - 1 + 5, +0

        seen = set()
        def traverse(node, prev):
            seen.add(node)
            print("checking", node, prev)
            if prev != None:
                ans[node] = ans[prev] - memo[node][1] + n - memo[node][1] 
                print(node, ans[node], ans[prev],memo[node])
            for nextNode in adjMap[node]:
                if nextNode in seen:
                    continue
                traverse(nextNode, node)
        traverse(0, None)
        return ans