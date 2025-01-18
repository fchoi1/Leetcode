class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        q = [(0,0,0)] # cost, x y
        seen = {}
        w = len(grid[0])
        h = len(grid)
        goal = (w-1,h-1)

        d = [(1,0), (-1,0), (0,1), (0, -1)]
        while q:
            cost, x, y = heappop(q)
            if (x,y) == goal:
                return cost
            
            if (x,y) in seen and seen[(x,y)] <= cost:
                continue
            seen[(x,y)] = cost
            
            for i, (dx, dy) in enumerate(d):
                newX = x + dx
                newY = y + dy
                if w > newX >= 0 and h > newY >= 0:
                    if i == grid[y][x] - 1:
                        heappush(q, (cost, newX, newY))
                    else:
                        heappush(q, (cost + 1, newX, newY))
        return -1
