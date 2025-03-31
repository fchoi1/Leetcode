class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        W = len(grid[0])
        H = len(grid)

        def traverse(x,y):
            if x < 0 or x >= W or y < 0 or y >= H or grid[y][x] == '0':
                return
            grid[y][x] = '0'
            for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                traverse(x+dx, y+dy)

        islands = 0
        for y in range(H):
            for x in range(W):
                if grid[y][x] == '1':
                    islands += 1
                    traverse(x,y)
        return islands
                