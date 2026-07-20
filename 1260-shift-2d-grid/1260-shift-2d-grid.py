class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        

        single = []
        W = len(grid[0])
        H = len(grid)

        for row in grid:
            single += row


        S = len(single)
        k = k % S
        single = (single + single)[S - k: S - k + S]
        ans = []
        for i in range(H):
            ans.append(single[i * W: (i * W) + W])
        
        return ans

        