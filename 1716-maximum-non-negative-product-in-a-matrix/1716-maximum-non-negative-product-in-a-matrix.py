class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # dp
        # keep max and min val
        W = len(grid[0])
        H = len(grid)

        dp = [[ ((grid[0][0], ''), (grid[0][0], '')) for _ in range(W)] for _ in range(H)]
        # (val, dir), (val, dir)

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if x == 0 and y == 0:
                    continue

                x_max, x_min, y_max, y_min = None, None, None, None

                if x > 0:
                    x_max, x_min = dp[y][x-1] 
                    curr_max, curr_max_dir = x_max
                    curr_min, curr_min_dir = x_min
                
                if y > 0:
                    y_max, y_min = dp[y-1][x]
                    curr_max, curr_max_dir = y_max
                    curr_min, curr_min_dir = y_min

                curr_max *= val
                curr_min *= val

                for m, d in [(x_max, 'R'), (x_min, 'R'), (y_max, 'D'), (y_min, 'D')]:
                    if m is None:
                        continue
                    if m[0] * val >= curr_max:
                        curr_max = m[0] * val
                        curr_max_dir = m[1] + d

                    if m[0] * val <= curr_min:
                        curr_min = m[0] * val
                        curr_min_dir = m[1] + d

                dp[y][x] = ((curr_max, curr_max_dir), (curr_min, curr_min_dir))
        

        return dp[-1][-1][0][0] % (10 ** 9 + 7) if dp[-1][-1][0][0] >= 0 else -1