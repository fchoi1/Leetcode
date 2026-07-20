class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        arr = [x for row in grid for x in row]

        k %= len(arr)
        arr = arr[-k:] + arr[:-k]

        return [arr[i*n:(i+1)*n] for i in range(m)]