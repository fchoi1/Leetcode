class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        self.W, self.H = len(grid[0]), len(grid)
        self.safe = [[inf for _ in range(self.W)] for _ in range(self.H)]   
    
        def traverse(x ,y):
            q = deque([(x,y)])
            seen = set()
            step = 0
            while q:
                for _ in range(len(q)):
                    x,y = q.popleft()

                    if (x,y) in seen or step >= self.safe[y][x]:
                        continue
                    seen.add((x,y))
                    self.safe[y][x] = step
                                        
                    for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:
                        if 0 <= x + dx < self.W and 0 <= y + dy < self.H and grid[y + dy][x + dx] != 1:
                            q.append((x + dx, y + dy))
                step += 1

        
        seen = set()
       

        for y in range(self.H):
            for x in range(self.W):
                if grid[y][x]:
                    traverse(x, y)
    
        # dfs
        q = [[-self.safe[0][0],0,0]]

        if grid[self.H-1][self.W-1] == 1:
            return 0

        while q:
            highest, x, y = heapq.heappop(q)
            curr = min(-highest, self.safe[y][x])
            if (x,y) == (self.W-1, self.H-1):
                return curr
            if (x,y) in seen:
                continue
            seen.add((x,y))         
            for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:
                if 0 <= x + dx < self.W and 0 <= y + dy < self.H and grid[y + dy][x + dx] != 1 and (x + dx, y + dy) not in seen:
                    heapq.heappush(q,(-curr, dx + x, dy + y))
        return 0
    