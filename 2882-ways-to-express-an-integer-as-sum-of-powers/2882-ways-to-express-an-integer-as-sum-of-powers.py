class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10 ** 9 + 7
        max_num = int(n ** (1 / x)) + 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, max_num + 1):
            power = i ** x
            for j in range(n, power - 1, -1):
                dp[j] = (dp[j] + dp[j - power]) % mod

        return dp[n]