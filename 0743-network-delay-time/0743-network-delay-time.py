class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adj = defaultdict(dict)
        for u,v,w in times:
            adj[u][v] = w
        #dijstras

        recieved = set()

        q = [(0, k)] # time, k
        latest = 0
        while q:
            time, currNode = heappop(q)

            if currNode in recieved:
                continue

            recieved.add(currNode)
            latest = time

            for nextNode, weight in adj[currNode].items():
                heappush(q, (time + weight, nextNode))
        
        if len(recieved) != n:
            return -1
        
        return latest

