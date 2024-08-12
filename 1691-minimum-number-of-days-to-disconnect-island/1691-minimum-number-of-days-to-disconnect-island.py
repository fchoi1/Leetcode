class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(x,y,seen):
            if (x,y) in seen or not grid[y][x]:
                return seen
            seen.add((x,y))
            for dx,dy in [(0,1), (0, -1), (1,0), (-1,0)]:
                if 0 <= x + dx < W and 0 <= y + dy < H:
                    seen = dfs(x+dx, y+dy, seen)
            return seen

        H = len(grid)
        W = len(grid[0])

        seen = set()
        count = sum(grid[y][x] for y in range(H) for x in range(W) )
        
        for y in range(H):
            for x in range(W):
                if grid[y][x] and (x,y) not in seen:
                    first = (x,y)
                    seen = dfs(x,y, set())
                    if len(seen) != count:
                        return 0
        if count == 0:
            return 0
        
        for y in range(H):
            for x in range(W):
                if grid[y][x]:
                    grid[y][x] = 0
                    if first == (x,y):
                        for dx,dy in [(0,1), (0, -1), (1,0), (-1,0)]:
                            if 0 <= x + dx < W and 0 <= y + dy < H and grid[y+dy][x+dx]:
                                seen = dfs(x+dx, y+dy, set())
                                break
                    else:
                        seen = dfs(*first, set())
                    if len(seen) != count - 1:
                        return 1
                    grid[y][x] = 1
        return 2
    
        
            
        