class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(grid[0]):
                if y > 0:
                    grid[y][x] += grid[y-1][x] 
                    if grid[y-1][x] > k:
                        continue
                if x > 0:
                    grid[y][x] += grid[y][x-1]
                    if grid[y][x-1] > k:
                        continue
                
                if x > 0 and y > 0:
                    grid[y][x] -= grid[y-1][x-1]

                if grid[y][x] <= k:
                    count += 1
        return count
        