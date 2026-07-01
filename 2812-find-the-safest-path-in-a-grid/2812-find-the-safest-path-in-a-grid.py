class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        W = len(grid[0])
        H = len(grid)

        costs = [ [inf for _ in range(W)] for _ in range(H)]
        for y in range(H):
            for x in range(W):
                if grid[y][x]:
                    costs[y][x] = 0
                    continue
                elif not x and not y:
                    continue
                elif not y:
                    costs[y][x] = 1 + costs[y-1][x]
                elif not x:
                    costs[y][x] = 1 + costs[y][x-1]
                else:
                    costs[y][x] = 1 + min(costs[y][x-1], costs[y-1][x])

        for y in range(H-1,-1,-1):
            for x in range(W-1,-1,-1):
                if x + 1 >= W and y + 1 >= H:
                    continue
                elif x + 1 >= W:
                    costs[y][x] = min(costs[y][x], 1 + costs[y+1][x])
                elif y + 1 >= H:
                    costs[y][x] = min(costs[y][x], 1 + costs[y][x+1])
                else:
                    costs[y][x] = min(costs[y][x], 1 + min(costs[y][x+1], costs[y+1][x]))


        q = [(-costs[0][0], 0, 0)]
        seen = set()
        while q:
            currCost, x, y = heapq.heappop(q)
            if (x,y) == (W-1, H-1):
                return -currCost

            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nX, nY = x + dx, y + dy
                if 0 <= nX < W and 0 <= nY < H and (nX, nY) not in seen:
                    seen.add((nX, nY))
                    heapq.heappush(q, (-min(costs[nY][nX], -currCost), nX, nY))

        return -1

       