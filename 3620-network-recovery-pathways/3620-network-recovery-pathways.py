class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # ignore offline nodes

        # dp
        # keep track of min edge, and cost 

        # top sort?
        if not edges:
            return -1

        adj = defaultdict(list)
        N = len(online)

        costs = set()
        for u,v,c in edges:
            costs.add(c)
            adj[u].append((v, c))

        def minCostToEnd(node, edgeCost, memo):
            if node == N - 1:
                return 0
            if node in memo:
                return memo[node]

            best = float('inf')
            for nextNode, nextCost in adj[node]:
                if nextCost < edgeCost or not online[nextNode]:
                    continue
                sub = minCostToEnd(nextNode, edgeCost, memo)
                if sub != float('inf'):
                    best = min(best, nextCost + sub)

            memo[node] = best
            return best

        l = 0
        r = len(costs) - 1

        costs = sorted(costs)

        while l <= r:
            mid = (l + r + 1) // 2
            memo = {}
            
            if minCostToEnd(0, costs[mid], memo) <= k:
                ans = costs[mid]
                l = mid + 1
            else:
                r = mid - 1
                if mid == 0:
                    return -1

        return ans



        