class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # dijstras

        adjMap = defaultdict(dict)
        for a,b,w in zip(original, changed, cost):
            adjMap[a][b] = min(adjMap[a].get(b,inf), w)

        
        costCache = {}
        
        @cache
        def getMinCost(source, target):
            heap = [(0, source)] # cost ,node

            seen = {}
            while heap:
                cost, node = heappop(heap)

                if node == target:
                    return cost
                
                if node in seen and seen[node] <= cost:
                    continue

                seen[node] = cost
                costCache[(source, node)] = cost

                for nextNode, nextCost in adjMap[node].items():
                    heappush(heap, (cost + nextCost, nextNode))

            return -1


        cost = 0
        for curr, new in zip(source, target):
            if curr == new:
                continue
            currCost = costCache.get((curr,new), getMinCost(curr,new))

            if currCost == -1:
                return -1
            
            cost += currCost

        return cost