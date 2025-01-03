class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        

        # low, high
        # zero, one 
        # zero zero
        # one one
        # one zero

        # recursion with cache
        # dp 
        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1

        for i in range(high):
            # zero
            zLen = i + zero
            oLen = i + one
            if zLen <= high:
                dp[zLen] += dp[i]
            if oLen <= high:
                dp[oLen] += dp[i]
            # print(zLen, oLen, 'index', i, dp)


        #     # one
        # print(dp)
        modulo = 10**9 + 7
        return sum(dp[low:high+1]) % modulo



