class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        
        def getNext(cell):
            r, d = divmod(cell - 1, N)
            x = d if r % 2 == 0 else N - 1 - d
            y = N - 1 - r
            return board[y][x] if board[y][x] != -1 else cell

        visited = set()
        queue = deque([(1, 0)])  # (cell, steps)

        while queue:
            cell, steps = queue.popleft()
            if cell == N * N:
                return steps
            for i in range(1, 7):
                next_cell = cell + i
                if next_cell > N * N:
                    continue
                dest = getNext(next_cell)
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, steps + 1))
                    
        return -1