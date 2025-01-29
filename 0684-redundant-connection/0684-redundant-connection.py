class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adjMap = defaultdict(set)
        for a,b in edges:
            adjMap[a].add(b)
            adjMap[b].add(a)

        self.seen = {}
        self.cycle = None

        def dfs(node, path):
            if node in self.seen:
                if not self.cycle:
                    self.cycle = path[self.seen[node]:] + [node]
                return
            self.seen[node] = len(path)
            for n in adjMap[node]:
                if path and n == path[-1]:
                    continue
                dfs(n, path + [node])
        dfs(1,[])

        e = set()
        for a,b in zip(self.cycle, self.cycle[1:]):
            e.add((min(a,b),max(a,b)))
        
        for a,b in edges[::-1]:
            if (min(a,b), max(a,b)) in e:
                return (a,b)

