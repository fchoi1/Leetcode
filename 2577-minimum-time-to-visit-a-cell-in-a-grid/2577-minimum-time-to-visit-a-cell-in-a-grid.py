class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # bfs
        
        q = [(0,0,0)]
        seen = set()
        h = len(grid)
        w = len(grid[0])
        goal = (h-1,w-1)
 
        
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        while q:
            temp = []
            steps, x, y = heapq.heappop(q)
            if (x,y) == (w-1, h-1):
                return steps
            
            if (x,y) in seen:
                continue
            seen.add((x,y))

            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                newX = x + dx
                newY = y + dy
                if 0 <= newX < w and 0 <= newY < h:
                    if steps + 1 >= grid[newY][newX]:
                        heapq.heappush(q, (steps + 1, newX, newY))
                    else:
                        diff = grid[newY][newX] - steps + 1
                        heapq.heappush(q, (grid[newY][newX] + int(diff % 2), newX, newY))
        return -1
        