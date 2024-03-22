class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[ [0] * n for _ in range(m)]
        dp[0][0] = 1

        for y in range(m):
            for x in range(n):
                if y > 0:
                    dp[y][x] += dp[y-1][x]
                if x > 0:
                    dp[y][x] += dp[y][x-1]
        return dp[m-1][n-1]
        