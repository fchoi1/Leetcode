class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
            
        def traverse(node, seen):
            seen.add(node)
            for nextNode in adj[node]:
                if nextNode not in seen:
                    seen = traverse(nextNode,seen)
            return seen
        
        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        total = 0
        for key in adj.keys():
            if key in visited:
                continue
            seen = traverse(key,set())
            visited.update(seen)
            total += len(seen) * (n-len(seen))
            n -= len(seen)
        total += int(n / 2 * (n - 1))

        return total

        
     

            
