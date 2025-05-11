class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        total = sum(sum(row) for row in grid)


        H = len(grid)
        W = len(grid[0])
        print(total)
        
        rowSum = 0
        
        for row in grid:
            rowSum += sum(row)

            if rowSum == total - rowSum:
                return True
        
        colSum = 0

        for i in range(W):
            colSum += sum(row[i] for row in grid)
            if colSum == total - colSum:
                return True

        return False
            