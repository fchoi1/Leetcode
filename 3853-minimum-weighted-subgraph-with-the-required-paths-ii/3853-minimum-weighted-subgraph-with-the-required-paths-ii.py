class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1  # Number of nodes
        
        # Step 1: Build adjacency list
        tree = defaultdict(list)
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))

        LOG = 17  # Since 2^17 > 1e5
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        dist = [0] * n  # Distance from root (node 0)

        # Step 2: DFS to fill depth and dist
        def dfs(u, p):
            for v, w in tree[u]:
                if v != p:
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    dfs(v, u)

        dfs(0, -1)

        # Step 3: Binary lifting preprocessing
        for k in range(1, LOG):
            for v in range(n):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]

        # Step 4: Function to compute LCA using binary lifting
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Lift u up to depth v
            for k in reversed(range(LOG)):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in reversed(range(LOG)):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        # Step 5: Compute distance between two nodes using LCA
        def get_dist(a, b):
            ancestor = lca(a, b)
            return dist[a] + dist[b] - 2 * dist[ancestor]

        result = []
        # Step 6: Process each query
        for src1, src2, dest in queries:
            d1 = get_dist(src1, src2)
            d2 = get_dist(src2, dest)
            d3 = get_dist(dest, src1)
            result.append((d1 + d2 + d3) // 2)
        return result