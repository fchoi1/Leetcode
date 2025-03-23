class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)

        for x,y, time in roads:
            adj[x].add((y, time))
            adj[y].add((x, time))
           
        count = 0
        seen = set()
        q = [(0,0,1)] # cost, node, dupes 
        shortest = None

        while q:
            cost, curr, dupes = heappop(q)

            while q and cost == q[0][0] and curr == q[0][1]:
                _,_,d = heappop(q)
                dupes += d

            if curr == n - 1:
                return dupes % (10 ** 9 + 7)
    
            if curr in seen: 
                continue

            seen.add(curr)

            for nextNode, time in adj[curr]:
                heappush(q, (cost + time, nextNode, dupes))
 
        return count

   