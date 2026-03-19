class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        W = len(grid[0])
        H = len(grid)
        dp = [[(0,0) for _ in range(W)] for _ in range(H)]
        ans = 0


        for y in range(H):
            for x in range(W):
                x_count = 0
                y_count = 0

                if grid[y][x] == 'X':
                    x_count += 1
                if grid[y][x] == 'Y':
                    y_count += 1

                
                
                if x > 0:
                    x_count += dp[y][x-1][0]
                    y_count += dp[y][x-1][1]

                if y > 0:
                    x_count += dp[y-1][x][0]
                    y_count += dp[y-1][x][1]

                if x > 0 and y > 0:
                    x_count -= dp[y-1][x-1][0]
                    y_count -= dp[y-1][x-1][1]


                if x_count == y_count and x_count > 0:
                    ans += 1
                
                dp[y][x] = (x_count, y_count)

        return ans