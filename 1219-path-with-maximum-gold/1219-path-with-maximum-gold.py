class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # backtrack
        W = len(grid[0])
        H = len(grid)
        maxGold = 0
        seen = set()
        def traverse(x,y, gold):
            nonlocal maxGold
            if (x,y) in seen or grid[y][x] == 0:
                maxGold = max(maxGold, gold)
                return
            seen.add((x,y))
            for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                if 0 <= x + dx < W and 0 <= y + dy < H:
                    traverse(x + dx, y + dy, gold + grid[y][x])
            seen.discard((x,y))
        for y in range(H):
            for x in range(W):
                if grid[y][x]:
                    traverse(x,y, 0)
               
        return maxGold