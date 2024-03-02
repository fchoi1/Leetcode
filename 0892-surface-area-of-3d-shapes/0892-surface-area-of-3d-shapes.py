class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total = 0
        w = len(grid[0])
        h = len(grid)
        for y,row in enumerate(grid):
            for x,n in enumerate(row):
                if n > 0:
                    # 6 sides subtract 2 sides for each connected cube
                    total += n * 6 - (n-1) * 2
                # check adjacent and subtract
                for dx, dy in [[0,1], [1,0]]:
                    if 0 <= x + dx < w and 0 <= y + dy < h:      
                        total -= min(n, grid[dy + y][ dx + x]) * 2
        return total 