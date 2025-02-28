class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #DP
        #Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
        #DP[i][j]

        # a
        # a -> 1


        # a 
        # b -> 0

        # a a c d
        # a b a e
        # arr[0][0] = 1
        # arr[1][1] = 1
        # arr[1][2] = 2
        # arr[1] [....] = 2
        # arr[2][2] = 2
        # arr[3] [....] = 2

        # N1 = len(text1)
        # N2 = len(text2)
        # dp = [[0 for _ in range(N2 + 1)] for _ in range(N1 + 1)]

        # for i in range(1, N1 + 1):
        #     for j in range(1, N2 + 1):
        #         print(text1[i-1], text2[j-1])
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = 1 + dp[i - 1][j -1]
        #         else:
        #             dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        # print(dp)

        # return dp[N1][N2]
        m = len(text1)
        n = len(text2)
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    memo[row][col] = 1 + memo[row - 1][col - 1]
                else:
                    memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])

        return memo[m][n]

        '''
        1 . . . . .
        . 1 2
        . 1 2
        . 
        .
        .
        '''