class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #dp

        N = len(word1)
        M = len(word2)

        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(1, M + 1):
            dp[i][0] = i

        for j in range(1, N + 1):
            dp[0][j] = j

        for i in range(1, M + 1):
            w2 = word2[i - 1]

            for j in range(1, N + 1):
                w1 = word1[j - 1]

                if w1 == w2:
                    dp[i][j] = dp[i-1][j-1]
                else:
            
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j])

        return dp[M][N]