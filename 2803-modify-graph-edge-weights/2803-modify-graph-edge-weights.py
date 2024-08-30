class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adj = defaultdict(dict)
        empty = set()
        for a,b,w in edges:
            if w == -1:
                empty.add((a,b))
            adj[a][b],adj[b][a] = w, w

        def dijkstra(start, target):
            q = [(0,start)]
            seen = set()
            while q:
                dist, curr = heapq.heappop(q)
                if curr == target:
                    return dist
                if curr in seen:
                    continue
                seen.add(curr)

                for next_node, w in adj[curr].items():
                    if w < 0:
                        continue
                    heapq.heappush(q, (max(1, w) + dist, next_node))
            else:
                return inf
            
        if dijkstra(source, destination) < target:
            return []
  
        for a,b in empty:
            adj[a][b], adj[b][a] = target,target
        
        if dijkstra(source, destination) > target:
            for a,b in empty:
                adj[a][b], adj[b][a] = 1,1
                shortest = dijkstra(source, destination)
                if shortest <= target:
                    value = target - shortest + 1
                    adj[a][b] = max(1,value)
                    adj[b][a] = max(1,value)
                    break
            else:
                return []

        for i in range(len(edges)):
            a,b, w = edges[i]
            edges[i] = [a,b,max(1,adj[a][b])]

        return edges