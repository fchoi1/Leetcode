class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # dfs 
        N = len(triangle)

        @lru_cache
        def dfs(index, row):
            return triangle[row][index] + min( dfs(index, row + 1), dfs(index + 1, row + 1)) if row < N else 0
       

        return dfs(0,0)