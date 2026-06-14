class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1) + 1
        M = len(word2) + 1

        dp = [[inf] * N  for _ in range(M)]  
        for i in range(N):
            dp[0][i] = i

        for i in range(M):
            dp[i][0] = i
        
        
        
        for y in range(1, M):
            for x in range(1, N):
                if word1[x - 1] == word2[y - 1]:
                    dp[y][x] = dp[y - 1][ x - 1]
                else:
                    dp[y][x] = 1 + min(dp[y-1][x], dp[y][x-1], dp[y - 1][x - 1])

        return dp[-1][-1]