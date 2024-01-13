class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        width = len(grid[0])
        height = len(grid)
        totalSeen = set()
        maxCount = 0
        def inRange(x, y):
            return 0 <= x < width and 0 <= y < height

        def dfs(pos, seen):
            x, y = pos
            if pos in seen or grid[y][x] == 0:
                return seen
            seen.add(pos)
            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                newX, newY = x + dx, y + dy
                if inRange(newX, newY):
                    dfs((newX, newY), seen)
            return seen

        for y in range(height):
            for x in range(width):
                if (x,y) in totalSeen or grid[y][x] == 0:
                    continue
                seen = dfs((x,y), set())
                totalSeen.update(seen)
                maxCount = max(maxCount, len(seen))
        return maxCount



        