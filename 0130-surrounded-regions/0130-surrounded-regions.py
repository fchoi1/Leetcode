class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        dirMap = [(0,-1),(0,1),(1,0),(-1,0)]
        m,n = len(board[0]), len(board)

        def bfs(coords):
            x, y = coords
            print(x, y)
            if coords in visited or board[y][x] == 'X':
                return
            visited.add(coords)
           
            for dx, dy in dirMap:
                if 0<= x+dx<m and 0 <= y+dy<n:
                    newCoords = (x+dx, y+dy)
                    if board[y + dy][x + dx] == 'O':
                        bfs(newCoords)

        xLines = [board[0], board[-1]]
        yLines = [x[0] for x in board], [x[-1] for x in board]
        for x in range(m):
            bfs((x,0))
            bfs((x,n-1))

        for y in range(n):
            bfs((0, y))
            bfs((m-1, y))

        for y in range(n):
            for x in range(m):
                if board[y][x] == "O" and (x,y) not in visited:
                    board[y][x] = "X" 
