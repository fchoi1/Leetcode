class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        for j in range(k//2):

            y1 = x + j
            y2 = x + k - j - 1

            for i in range(y,y + k):
                print(y1, y2, i, len(grid), len(grid[0]))
                grid[y1][i], grid[y2][i] = grid[y2][i], grid[y1][i]

        return grid