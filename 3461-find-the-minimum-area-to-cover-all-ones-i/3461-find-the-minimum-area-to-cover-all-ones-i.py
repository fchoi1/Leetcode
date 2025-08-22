class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # scan top bottom, left, rgith

        H = len(grid)
        W = len(grid[0])

        minRow = H - 1
        maxRow = 0
        minCol = W - 1
        maxCol = 0
        for j in range(H):
            for i in range(W):
                if grid[j][i] == 1:
                    minRow = min(minRow, j)
                    maxRow = max(maxRow, j)
                    minCol = min(minCol, i)
                    maxCol = max(maxCol, i)
        if maxCol < minCol or maxRow < minRow:
            return 0
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)

