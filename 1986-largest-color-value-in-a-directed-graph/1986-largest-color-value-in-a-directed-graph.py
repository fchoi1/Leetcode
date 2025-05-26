class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        adj = defaultdict(set)
        for a,b in edges:
            if a == b:
                return -1
            adj[a].add(b) 
 
        n = len(colors)
        start = set(range(n))
        for i in range(n):
            if i in adj:
                for node in adj[i]:
                    start.discard(node)    
        visited = set()

        cache = {} # node: max counts

        def dfs(node):
            visited.add(node)

            if node in cache:
                return cache[node]
            
            cache[node] = None
            
            counts = [0] * 26

            for child in adj[node]:
                res = dfs(child)
                if res == None:
                    return None
                for i in range(26):
                    counts[i] = max(counts[i], res[i])
            
            index = ord(colors[node]) - ord('a')
            counts[index] += 1
            cache[node] = counts
            return counts

        c = 0
        for node in start:
            res = dfs(node)
            if res == None:
                return -1
            c = max(c, max(res))
       
        if len(visited) != n:
            return -1

        return c