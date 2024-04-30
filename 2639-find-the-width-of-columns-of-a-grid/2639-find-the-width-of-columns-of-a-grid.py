class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        N = len(grid[0])
        ans = [0 for _ in range(N)]
        for row in grid:
            for i,col in enumerate(row):
                ans[i] = max(ans[i], len(str(col)))
        return ans
        