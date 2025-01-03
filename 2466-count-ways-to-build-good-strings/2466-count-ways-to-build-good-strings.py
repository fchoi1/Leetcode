class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        

        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1

        curr = 0
        modulo = 10**9 + 7

        for i in range(high + 1):
            # zero
            zLen = i + zero
            oLen = i + one
            if zLen <= high:
                dp[zLen] += dp[i]
            if oLen <= high:
                dp[oLen] += dp[i]
            if i >= low :
                curr += dp[i] 

        return curr % modulo



