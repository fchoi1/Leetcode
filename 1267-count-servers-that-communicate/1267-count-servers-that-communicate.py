class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        W = len(grid[0])
        H = len(grid)
        rows = [set() for _ in range(H)]
        cols = [set() for _ in range(W)]

        for y in range(H):
            for x in range(W):
                if grid[y][x]:
                    rows[y].add((x,y))
                    cols[x].add((x,y))
        
        communicate = set()

        for r in rows:
            if len(r) > 1:
                communicate |= r

        for c in cols:
            if len(c) > 1:
                communicate |= c

        return len(communicate)


        