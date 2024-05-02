class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        W = len(obstacleGrid[0])
        H = len(obstacleGrid)
        dp = [[0 for _ in range(W)] for _ in range(H)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for y, row in enumerate(obstacleGrid):
            for x, val in enumerate(row):
                if val:
                    continue
                if y > 0:
                    dp[y][x] += dp[y-1][x] 
                if x > 0:
                    dp[y][x] += dp[y][x-1] 
        return dp[H-1][W-1]
        