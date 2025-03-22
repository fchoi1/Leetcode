class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj = defaultdict(set)

        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)

        def traverse(node):
            if node in seen:
                return
            seen.add(node)
            
            for nextNode in adj[node]:
                seen.add(nextNode)
                if adj[node] | set([node]) != adj[nextNode] | set([nextNode]):
                    return False
            return True

        count = 0
        for i in range(n):
            if i not in seen:
                if traverse(i):
                    count += 1

        return count