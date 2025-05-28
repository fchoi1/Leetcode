class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj1 = defaultdict(set)
        adj2 = defaultdict(set)

        for a,b in edges1:
            adj1[a].add(b)
            adj1[b].add(a)

        for a,b in edges2:
            adj2[a].add(b)
            adj2[b].add(a)

        def countNodes(node, dist, adj):
            seen = set()
            def dfs(n, length):
                if n in seen or length > dist:
                    return 
                seen.add(n)

                for nextNode in adj[n]:
                    dfs(nextNode, length + 1)
            
            dfs(node, 0)
                
            return len(seen)

        
        # m length
        max_m = 0
        for i in range(m):
            counts = countNodes(i, k-1, adj2)
            max_m = max(max_m, counts)
        
        ans = []
        for i in range(n):
            count = countNodes(i, k, adj1)
            ans.append(count + max_m)
        return ans
