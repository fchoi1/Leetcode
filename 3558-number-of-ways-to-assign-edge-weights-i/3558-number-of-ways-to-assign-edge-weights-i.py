class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        
        # get max depth
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def getDepth(node, seen):
            d = 0
            seen.add(node)
            for n in adj[node]:
                if n in seen:
                    continue
                d = max(getDepth(n, seen), d)

            return d + 1
 
        depth = getDepth(1, set())
        MOD = 10**9 + 7
        return pow(2, depth - 2, MOD)