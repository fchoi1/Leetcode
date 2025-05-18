class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        dir = [(0,1), (1,0), (-1,0), (0,-1)]
        W = len(matrix[0])
        H = len(matrix)

        portal = defaultdict(set)

        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val not in "#.":
                    portal[val].add((x,y))
     
        
        q = deque([(0,0,0, set())]) # cost, x,y , portal

        steps = 0
        seen = {}
        while q:            
            cost,x,y,letters = q.popleft()
            cell = matrix[y][x]

            if (x,y) == (W-1, H-1):
                return cost 
                
            if (x,y) in seen and seen[(x,y)] <= cost:
                continue
                
            seen[(x,y)] = cost

            if cell not in letters:
                for (lx, ly) in portal[cell]:
                    if (lx, ly) == (W-1, H-1):
                        return cost
                    t = letters.copy()
                    t.add(cell)
                    q.appendleft((cost, lx, ly, t))
                    
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < W and 0 <= ny < H and matrix[ny][nx] != '#':
                    q.append((cost + 1, nx, ny, letters))
                
        return -1
                

        