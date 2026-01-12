class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dfs 

        H = len(matrix)
        W = len(matrix[0])

        @cache
        def dfs(row, col):
            
            # base case
            if row == H-1:
                return matrix[row][col]
            minSum = inf
            for i in range(-1,2):
                if col + i >= 0 and col + i < W:
                    minSum = min(minSum,dfs(row + 1, col + i))
            return minSum + matrix[row][col]
        
        ans = inf
        for c in range(W):
            ans = min(ans, dfs(0, c))

        return ans

            
        