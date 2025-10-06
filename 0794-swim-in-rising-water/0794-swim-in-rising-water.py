class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # min time from each grid to end

        cache = {}

        # bfs
        N = len(grid)
        end = (N-1, N-1)

        heap = [(grid[N-1][N-1], end)] # height, pos
        seen = set()

        while heap:
            h, (x,y) = heappop(heap)
            if (x,y) in seen:
                continue
            seen.add((x,y))
            if (x,y) == (0,0):
                return h

            for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                
                    heappush(heap, (max(h, grid[ny][nx]), (nx, ny)))
        print("errro")   
        return -1
