class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # max path with 2 skips

        # dp tuple  (max w/o skip, 1 skip, 2 skips)

        W = len(coins[0])
        H = len(coins)
        dp = [[(-inf, -inf, -inf) for _ in range(W)] for _ in range(H)]
        
        
        dp[0][0] = (coins[0][0], 0, -inf)


        for y, row in enumerate(coins):
            for x, val in enumerate(row):

                if x == 0 and y == 0:
                    continue
                
                curr_1, curr_2, curr_3  = dp[y][x]

                if y > 0:
                    y_1, y_2, y_3 = dp[y-1][x]
                    curr_1, curr_2, curr_3 = (y_1 + val, max(y_2 + val, y_1), max(y_3 + val, y_2))

                if x > 0:
                    x_1, x_2, x_3 = dp[y][x-1]
                    curr_1, curr_2, curr_3  = (max(x_1 + val, curr_1), max(x_2 + val, x_1, curr_2), max(x_3 + val, x_2, curr_3))

                dp[y][x] = (curr_1, curr_2, curr_3 )

        return max(dp[-1][-1])