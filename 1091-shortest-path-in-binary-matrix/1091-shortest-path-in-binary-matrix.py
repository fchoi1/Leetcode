class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        q = deque([(0,0)])
        steps = 1
        seen = set()
        N = len(grid)
        def inRange(x, y):
            return 0 <= x < N and 0 <= y < N

        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                if x == N - 1 and y == N - 1:
                    return steps
                if (x,y) in seen:
                    continue
                seen.add((x,y))
                for dx, dy in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,1],[-1,-1],[1,-1]]:
                    newX, newY = x + dx, y + dy
                    if inRange(newX, newY) and not grid[newY][newX]:
                        q.append((newX, newY))
            steps += 1
        return -1
        

