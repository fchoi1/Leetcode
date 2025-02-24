class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        # alice has to go to the optimal leaf?
        print("edges", len(edges))
        adjMap = defaultdict(set)

        for a,b in edges:
            adjMap[a].add(b)
            adjMap[b].add(a)
        
        # find leaf nodes?
        leaf = set()
        for node, childs in adjMap.items():
            if len(childs) == 1:
                leaf.add(node)
        
        # get path of bob
        # backtrack cause MLE
        self.bobPath = []
        def findPath(node, path, seen):
            if node == 0:
                self.bobPath = path[::]
                return True

            seen.add(node)
            for n in adjMap[node]:
                if n in seen:
                    continue
                path.append(n)
                if findPath(n, path, seen):
                    return True
                path.pop()
            return False

        findPath(bob, [bob], set())
        bobDict = { node:i for i, node in enumerate(self.bobPath)}

        # bfs 

        q = deque([(0, 0, 0)]) # node, amount, step
        seen = set()
        maxIncome = -inf
        while q:
            node, total, time = q.popleft()
            # print(node, total, time)
            if node in seen:
                continue
            seen.add(node)

            if node not in bobDict or bobDict[node] > time:
                total += amount[node]
            elif bobDict[node] == time:
                total += amount[node] / 2 
           
            if node in leaf and node != 0:
                maxIncome = max(maxIncome, total)
                continue

            for n in adjMap[node]:
                q.append((n, total, time + 1))

        return int(maxIncome)
        