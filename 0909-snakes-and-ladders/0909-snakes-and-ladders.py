class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        seen = {}
        N = len(board)
        MAX_CELL = N ** 2 

        def getNextCell(cell):
            r , d = divmod(cell - 1 ,  N)
            
            if r % 2 == 0:
                x = d 
            else:
                x = N - d - 1

            y = N - 1 - r
            return board[y][x] if board[y][x] != -1 else cell
            
        @cache
        def dfs(cell, step):

            if cell == MAX_CELL:
                return step 

            if cell in seen and step >= seen[cell]:
                return inf
            seen[cell] = step
            steps = inf

            for i in range(6):
                nextCell = getNextCell(min(cell + 1 + i, MAX_CELL))
                steps = min(steps, dfs(nextCell, step + 1))

            return steps

        steps = dfs(1,0)
        return steps if steps != inf else -1