class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)

        for start, end, price in flights:
            adj[start].append((end, price))

        q = deque([(src, 0)])
        steps = 0
        cheapest = float('inf')
        seen = defaultdict(lambda: float('inf'))
        while q and steps <= k + 1:
            
            for i in range(len(q)):
                curr, price = q.popleft()

                if curr in seen:
                    if price < seen[curr]:
                        seen[curr] = price
                    else:
                        continue
                seen[curr] = price
                if price > cheapest:
                    continue
                if curr == dst:
                    cheapest = min(cheapest, price)
                    continue
                for node, p in adj[curr]:
                    q.append((node,price+p))
            steps += 1
        return cheapest if cheapest != float('inf') else -1