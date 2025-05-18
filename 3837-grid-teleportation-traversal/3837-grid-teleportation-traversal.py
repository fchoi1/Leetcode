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
     
        
        q = deque([(0,0,0)]) # cost, x,y , portal

        steps = 0
        seen = set()
        used = set()
        while q:            
            cost,x,y = q.popleft()
            cell = matrix[y][x]

            if (x,y) == (W-1, H-1):
                return cost 

            if cell not in '#.' and cell not in used:
                used.add(cell)
                for (lx, ly) in portal[cell]:
                    if (lx, ly) == (W-1, H-1):
                        return cost
                    q.appendleft((cost, lx, ly))
                    
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if (nx,ny) in seen:
                    continue
                    
                seen.add((nx,ny))
                if 0 <= nx < W and 0 <= ny < H and matrix[ny][nx] != '#':
                    q.append((cost + 1, nx, ny))
                
        return -1
                

        