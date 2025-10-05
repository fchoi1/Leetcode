class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs on each? 
        # dp to track seen (pacific, atlantic)

        cache = {}
        both = []

        W = len(heights[0])
        H = len(heights)
        p = []
        # bfs 

        def bfs(x,y,reach):
            q = [(x,y)]

            while q:
                temp = []
                for x,y in q:
                    if (x,y) in reach:
                        continue
                    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < W and 0 <= ny < H:
                            if heights[ny][nx] >= heights[y][x]:
                                temp.append((nx, ny))
                        reach.add((x,y))
                q = temp
        p = set()
        a = set()
        for x in range(W):
            bfs(x,0,p)
            bfs(x,H-1,a)
        for y in range(H):
            bfs(0,y,p)
            bfs(W-1,y,a)

        for y in range(H):
            for x in range(W):
                if (x,y) in p and (x,y) in a:
                    both.append((y,x))
        return both