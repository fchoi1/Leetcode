class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        width, length = len(grid[0]), len(grid)
        visited = set()
        def dfs(pos, perimeter):
            x, y = pos

            if pos in visited:
                return perimeter
                
            if not (0 <= x < width and 0 <= y < length) or grid[y][x] == 0:
                return perimeter + 1

            visited.add(pos)
            for dx, dy in directions:
                perimeter = dfs((x + dx, y + dy), perimeter)
            
            return perimeter

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    ans = dfs((x,y), 0)
                    return ans
        
        return -1