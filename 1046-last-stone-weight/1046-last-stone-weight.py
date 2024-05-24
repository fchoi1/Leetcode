class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-w for w in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if x == y:
                continue
            heapq.heappush(stones,y-x)
        
        return -stones[0] if stones else 0
        