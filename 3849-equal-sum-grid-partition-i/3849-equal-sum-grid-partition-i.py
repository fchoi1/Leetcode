class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        rows = [sum(r) for r in grid]
        total = sum(rows)
        
        curr = 0
        for r in rows:
            curr += r
            if curr == total - curr:
                return True

        cols = [sum(r[i] for r in grid) for i in range(len(grid[0]))]
        curr = 0
        for c in cols:
            curr += c
            if curr == total - curr:
                return True
        print(rows, cols)
        return False