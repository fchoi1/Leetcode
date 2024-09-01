class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = defaultdict(dict)
        for (a,b), p in zip(edges,succProb):
            adj[a][b] = p
            adj[b][a] = p
        

        q = [(-1, start_node)]
        visited = defaultdict(int)
        while q:
            # print(q)
            prob, curr = heapq.heappop(q)
            prob = -prob

            if curr == end_node:
                return prob
            
            if curr in visited and prob <= visited[curr]:
                continue
            
            visited[curr] = prob

            for next_node, p in adj[curr].items():
                heapq.heappush(q, (p *-prob, next_node))

            
        return 0
            

