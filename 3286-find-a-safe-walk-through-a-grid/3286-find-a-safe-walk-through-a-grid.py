class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # min cost to bottom
        # dijstras

        q = [(grid[0][0], (0,0))] # cost and x,y
        seen = set()
        W = len(grid[0])
        H = len(grid)

        while q:
            cost, (x, y) = heappop(q)
            if (x,y) in seen:
                continue
            seen.add((x,y))

            if (x, y) == (W - 1, H - 1):
                return health > cost

            for dx, dy in [(0,1), (1,0), (-1, 0), (0, -1)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < W and 0 <= ny < H:
                    heappush(q, (cost + grid[ny][nx], (nx, ny)))
        print("error")
        return None


