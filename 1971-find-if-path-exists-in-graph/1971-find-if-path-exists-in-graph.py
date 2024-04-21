class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjMap = defaultdict(set)
        for a,b in edges:
            adjMap[a].add(b)
            adjMap[b].add(a)
        
        seen = set()
        node = source
        
        def traverse(node):
            if node in seen:
                return False
            if node == destination:
                return True
            seen.add(node)
            for n in adjMap[node]:
                if traverse(n):
                    return True
            return False
        
        return traverse(source)

        