class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        

        H = len(heightMap)
        W = len(heightMap[0])
        boundary = []
        edges = set()
        for i in range(W):
            heappush(boundary, (heightMap[0][i], i, 0))
            heappush(boundary, (heightMap[H-1][i], i, H-1))
            edges.add((i,0))
            edges.add((i, H-1))

        for i in range(1,H-1):
            heappush(boundary, (heightMap[i][0], 0, i))
            heappush(boundary, (heightMap[i][W-1], W-1, i))
            edges.add((0, i))
            edges.add((W-1, i))
        
        seen = set()
        rain = 0
        while len(boundary) > 0:
            h, x, y = heappop(boundary)
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                newX = x + dx
                newY = y + dy
                if H > newY >= 0 and W > newX >= 0 and (newX, newY) not in edges and (newX, newY) not in seen:
                    if heightMap[newY][newX] < h:
                        rain += h - heightMap[newY][newX]
                    seen.add((newX, newY))
                    heappush(boundary, (max(heightMap[newY][newX], h),newX, newY))

        return rain
