class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def bfs(start, min_length):
            cities = set()
            q = [(0, start)]
            while q:
                dist, curr = heapq.heappop(q)
                if curr in cities:
                    continue
                if start != curr:
                    cities.add(curr)
                    if len(cities) > min_length:
                        return len(cities)
            
                if curr in nodes:
                    for n in nodes[curr]:
                        if dist + nodes[curr][n] <= distanceThreshold:
                            heapq.heappush(q, (dist + nodes[curr][n], n))
            return len(cities)

        nodes = {}
        for a,b,w in edges:
            if a not in nodes:
                nodes[a] = {}
            if b not in nodes:
                nodes[b] = {}
            
            nodes[a][b] = w
            nodes[b][a] = w
        
        min_reach = inf
        min_city = None

        for i in range(n):
            curr_length = bfs(i,min_reach)
            if curr_length <= min_reach:
                min_reach = curr_length
                min_city = i

        return min_city



        