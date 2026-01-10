class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        h = []

        for s in stones:
            heappush(h, -s)


        while len(h) >= 2:
            one = heappop(h)
            two = heappop(h)
            if one == two:
                continue
            
            heappush(h, -abs(one-two))
        
        return 0 if not h else -h[0]