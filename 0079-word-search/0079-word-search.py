class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        W,H = len(board[0]), len(board)

        def inRange(x,y):
            return 0 <= x < W and 0 <= y < H
        
        def traverse(x,y, index, seen):
            if index >= len(word) or word[index] != board[y][x] or (x,y) in seen:
                return False
            if index == len(word) - 1:
                return True
            seen.add((x,y))
            for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                if inRange(x+dx, y+dy) and traverse(x+dx, y+dy, index + 1, seen):
                        return True
            seen.remove((x,y))
            return False
            
        for y, row in enumerate(board):
            for x, row in enumerate(row):
                if board[y][x] == word[0]:
                    if traverse(x,y,0,set()):
                        return True
        return False

        