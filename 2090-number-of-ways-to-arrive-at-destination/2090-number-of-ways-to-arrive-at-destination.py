class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(dict)

        for x,y, time in roads:

            if y in adj[x]:
                adj[x][y] = min(adj[x][y], time)
            else:
                adj[x][y] = time

            if x in adj[y]:
                adj[y][x] = min(adj[y][x], time)
            else:
                adj[y][x] = time
        
        mod = (10 ** 9 + 7)
        seen = set()
        q = [(0,0,1)] # cost, node, dupes 
        shortest = None

        while q:
            cost, curr, dupes = heappop(q)

            while q and cost == q[0][0] and curr == q[0][1]:
                _,_,d = heappop(q)
                dupes += d

            if curr == n - 1:
                return dupes % mod
    
            if curr in seen: 
                continue

            seen.add(curr)

            for nextNode, time in adj[curr].items():
                heappush(q, (cost + time, nextNode, dupes % mod))
 
        return count

   