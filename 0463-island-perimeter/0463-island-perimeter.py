class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        H = len(grid)
        W = len(grid[0])
        perimeter = 0
        for y in range(H):
            for x in range(W):
                if not grid[y][x]:
                    continue
                for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
                    if not (0 <= x + dx < W and 0 <= y + dy < H) or not grid[dy + y][dx + x]:
                        perimeter += 1        
        return perimeter