class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        # bfs
        def getfish(q):
            fish = 0
            while q:
                x,y = q.popleft()

                fish += grid[y][x]
                grid[y][x] = 0
                
                for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    newX, newY = x + dx, y + dy
                    if H > newY >= 0 and W > newX >= 0 and grid[newY][newX] > 0:
                        q.append((newX, newY))
            return fish
                    

        W = len(grid[0])
        H = len(grid)

        maxFish = 0
        for y in range(H):
            for x in range(W):
                if grid[y][x]:
                    maxFish = max(maxFish, getfish(deque([(x,y)])))
        return maxFish

        
                

