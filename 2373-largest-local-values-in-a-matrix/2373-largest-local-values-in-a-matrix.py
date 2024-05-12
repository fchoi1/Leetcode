class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        length = len(grid)

        def getMax(x,y):
            val = grid[y][x]
            for dx, dy in [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,-1),(-1,1)]:
                val = max(val, grid[y+dy][x+dx])
            return val

        for y in range(1,length-1):
            row = []
            for x in range(1,length-1):
                row.append(getMax(x,y))
            res.append(row)
        return res