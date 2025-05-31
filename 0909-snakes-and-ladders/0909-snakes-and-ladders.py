class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)

        def get_next(cell):
            r, d = divmod(cell - 1, N)
            x = d if r % 2 == 0 else N - 1 - d
            y = N - 1 - r
            return board[y][x] if board[y][x] != -1 else cell

        visited = set()
        heap = [(0, 1)]  # (steps, cell)

        while heap:
            steps, cell = heapq.heappop(heap)
            if cell == N * N:
                return steps
            if cell in visited:
                continue
            visited.add(cell)

            for i in range(1, 7):
                next_cell = cell + i
                if next_cell > N * N:
                    continue
                dest = get_next(next_cell)
                if dest not in visited:
                    heapq.heappush(heap, (steps + 1, dest))

        return -1