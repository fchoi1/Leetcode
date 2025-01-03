class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        

        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1

        curr = 0
        modulo = 10**9 + 7

        for i in range(high + 1):
            zLen = i + zero
            oLen = i + one
            if zLen <= high:
                dp[zLen] =  (dp[zLen] + dp[i]) % modulo
            if oLen <= high:
                dp[oLen] = (dp[oLen] + dp[i]) % modulo
            dp[i] = dp[i] % modulo
            if i >= low :
                curr = (curr + dp[i]) % modulo
        return curr



