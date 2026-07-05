class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # connected component


        visited = set()
        adj = defaultdict(list)
        min_dist = inf

        for a,b, d in roads:
            adj[a].append((b,d))
            adj[b].append((a,d))

        def dfs(node):
            nonlocal min_dist
            if node in visited:
                return
            visited.add(node)

            for nextNode, dist in adj[node]:
                min_dist = min(min_dist, dist)
                dfs(nextNode)

        dfs(1)
        if n not in visited:
            return -1

        return min_dist