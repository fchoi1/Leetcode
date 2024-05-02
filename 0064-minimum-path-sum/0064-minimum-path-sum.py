class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        W = len(grid[0])
        H = len(grid)
        prevRow = [float('inf') for _ in range(W)]
        for y, row in enumerate(grid):
            newRow = []
            prevVal = float('inf')
            for x, val in enumerate(row):
                currVal = val
                if x > 0 or y > 0:
                    currVal += min(prevVal, prevRow[x])
                newRow.append(currVal)
                prevVal = currVal
            prevRow = newRow
        return prevRow[-1]