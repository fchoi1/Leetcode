class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        dirMap = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,1],[-1,-1],[1,-1]]
        
        for y, row in enumerate(board):
            for x,  n in enumerate(row):
                live = 0
                for dx, dy in dirMap:
                    newX, newY = x + dx, y + dy
                    if 0 <= newX < len(row) and  0 <= newY < len(board):
                        if board[newY][newX] == 1 or board[newY][newX] == 3:
                            live += 1
                if n == 1 and live < 2:
                    board[y][x] = 1
                elif n == 1 and live < 4:
                    board[y][x] = 3
                elif n == 1:
                    board[y][x] = 1
                elif n == 0 and live == 3:
                    board[y][x] = 2
                    
        for y, row in enumerate(board):
            for x, n in enumerate(row):
                if n == 1:
                    board[y][x] = 0
                elif n == 2:
                    board[y][x] = 1
                elif n == 3:
                    board[y][x] = 1
                    
                
                 
        
        
        
        