class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # always flip once if len is not
        rows = len(grid)
        cols = len(grid[0])
        for i, row in enumerate(grid):
            if row[0] == 0:
                grid[i] = [0 if x else 1 for x  in grid[i]]
        
        # count a switch majoritity
        maxScore = 0 
        for i in range(cols):
            count = Counter(row[i] for row in grid)
            val = max(count[0], count[1])
            maxScore += val * (2**(cols-1-i))
        return maxScore