class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        W = len(matrix[0])
        H = len(matrix)
        minSum = float("inf")
        dpGrid = [[float("inf")] * W for _ in range(H)]

        def inRange(x):
            return 0 <= x < W

        def dfs(level, x):
            if level == H:
                return 0

            if dpGrid[level][x] != float("inf"):
                return dpGrid[level][x]

            minPathSum = matrix[level][x] + min(
                dfs(level + 1, x + dx)
                for dx in [-1, 0, 1]
                if inRange(x + dx)
            )

            dpGrid[level][x] = minPathSum
            return minPathSum

        minSum = min(dfs(0, x) for x in range(W))
        return minSum

                