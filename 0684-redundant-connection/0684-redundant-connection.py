class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, path, seen, prev,):
            nonlocal loop
            if loop:
                return
            if node in seen:
                if path[0] == path[-1]:
                    loop = path.copy()
                return
            seen.add(node)
            for n in adjMap[node]:
                if n == prev:
                    continue
                path.append(n)
                dfs(n, path, seen, node)
                path.pop()
            seen.remove(node)

        adjMap = defaultdict(set)
        for a,b in edges:
            adjMap[a].add(b)
            adjMap[b].add(a)
        
        loop = None
        for i in range(len(edges)):
            if loop:
                break
            dfs(i+1, [i+1], set(), None)
        # print(loop)
        edgesSet = set()
        for a,b in zip(loop, loop[1:]):
            edgesSet.add((min(a,b), max(a,b)))
        edgesSet.add((min(loop[0], loop[-1]), max(loop[0], loop[-1])))

        extra = None
        print(edgesSet)
        for a,b in edges:
            if (min(a,b), max(a,b)) in edgesSet:
                extra = [a,b]

        return extra
