class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        alantic = set()
        width = len(heights[0])
        height = len(heights)

        def inBounds(x,y):
            return 0 <= x < width and 0 <= y < height

        def dfs(pos, seen, prevHieght):
            x,y = pos
            currHeight = heights[y][x]
            if pos in seen or currHeight < prevHieght:
                return
            seen.add(pos)
            for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                newX, newY = x + dx, y + dy
                if inBounds(newX, newY):
                    dfs((newX, newY), seen, currHeight)

        for x in range(width):
            dfs((x,0), pacific, 0)
            dfs((x, height-1), alantic, 0)

        for y in range(height):
            dfs((0,y), pacific, 0)
            dfs((width-1, y), alantic, 0)

        res = []
        for y in range(height):
            for x in range(width):
                pos = (x, y)
                if pos in alantic and pos in pacific:
                    res.append([y,x])
        return res