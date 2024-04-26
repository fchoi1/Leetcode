class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if N == 1:
            return grid[0][0]

        dp = [[None for _ in range(N)] for _ in range(N)]
        prev = None
        for y in range(N):
            row = prev if prev else grid[y]
            first = min(row[0], row[1])
            second = max(row[0], row[1])
            for val in row[2:]:
                if val < first:
                    first, second = val, first
                elif val  < second:
                    second = val
            nextRow = []
            for x in range(N):
                if prev:
                    if prev[x] == first:
                        nextRow.append( grid[y][x] + second)
                    else:
                        nextRow.append( grid[y][x]  + first)
            if not prev:
                prev = grid[y]
            else:
                prev = nextRow
            print("row", y, first, second)
            print(prev)
        return min(prev)
                    
                
                    
    
        return 1