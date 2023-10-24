class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        dirMap = [(0,-1),(0,1),(1,0),(-1,0)]
        noFlip = set()
        m,n = len(board[0]), len(board)

        def bfs(coords):
            if coords in visited:
                return
            visited.add(coords)
            noFlip.add(coords)
            x, y = coords
            for dx, dy in dirMap:
                if 0<= x+dx<m and 0 <= y+dy<n:
                    newCoords = (x+dx, y+dy)
                    if board[y + dy][x + dx] == 'O':
                        bfs(newCoords)

        xLines = [board[0], board[-1]]
        yLines = [x[0] for x in board], [x[-1] for x in board]
        for y,line in enumerate(xLines):
            for x, char in enumerate(line):
                if char == "O":
                    bfs((x,[0,n-1][y]))

        for x,line in enumerate(yLines):
            for y, char in enumerate(line):
                if char == "O":
                    bfs(([0,m-1][x], y))

        for y in range(n):
            for x in range(m):
                if board[y][x] == "O" and (x,y) not in noFlip:
                    board[y][x] = "X" 
