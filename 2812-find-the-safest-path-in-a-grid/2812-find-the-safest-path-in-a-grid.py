class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N =  len(grid)
        self.safe = [[inf for _ in range(N)] for _ in range(N)]   
    
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
                        if 0 <= x + dx < N and 0 <= y + dy < N and grid[y + dy][x + dx] != 1 and (x + dx, y + dy) not in seen:
                            q.append((x + dx, y + dy))
                step += 1

        seen = set()
       
        for y in range(N):
            for x in range(N):
                if grid[y][x]:
                    traverse(x, y)
    
        # dfs
        q = [[-self.safe[0][0],0,0]]

        while q:
            highest, x, y = heapq.heappop(q)
            curr = min(-highest, self.safe[y][x])
            if (x,y) == (N-1, N-1):
                return curr

            if (x,y) in seen:
                print("hih", x,y)
                continue
            seen.add((x,y))         
            for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:
                if 0 <= x + dx < N and 0 <= y + dy < N and grid[y + dy][x + dx] != 1:
                    heapq.heappush(q,[-curr, dx + x, dy + y])
        return 0
    