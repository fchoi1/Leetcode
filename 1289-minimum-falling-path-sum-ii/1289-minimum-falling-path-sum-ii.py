class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if N == 1:
            return grid[0][0]
        prev = grid[0]
        for y in range(1,N):
            first = min(prev[0], prev[1])
            second = max(prev[0], prev[1])

            for val in prev[2:]:
                if val < first:
                    first, second = val, first
                elif val < second:
                    second = val
            nextRow = []
            for x in range(N):
                val = second if prev[x] == first else first
                nextRow.append(grid[y][x] + val)
            prev = nextRow
         
        return min(prev)
                    
                
                    
    
        return 1