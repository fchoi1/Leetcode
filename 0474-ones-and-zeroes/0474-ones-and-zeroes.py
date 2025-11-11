class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            if zeros > m or ones > n:
                continue

            # get max in grid
            max_count = 0
            for y in range(n, ones - 1, -1):
                for x in range(m, zeros - 1, -1):
                    max_count = max(max_count, dp[y][x])
                    dp[y][x] = max(dp[y][x], 1 + dp[y - ones][x - zeros])

        return dp[-1][-1]