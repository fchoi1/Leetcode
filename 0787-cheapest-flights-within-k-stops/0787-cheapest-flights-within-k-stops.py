class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)

        for start, end, price in flights:
            adj[start].append((end, price))

        q = [(0,src,0)]
        visited = {}
        
        while q:
            price, curr, stops = heappop(q)
            if curr == dst:
                return price
            
            if stops > k or (curr in visited and visited[curr] <= stops):
                continue
            visited[curr] = stops

            for n,p in adj[curr]:
                heappush(q, (p + price, n, stops + 1))
        
        return -1
