class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def checkSquare(x,y):
            seen = set()
            target = sum(grid[y][x:x+3])
            for i in range(3):
                seen = seen.union(grid[y + i][x:x+3])
                if sum(grid[y + i][x:x+3]) != target:
                    return False
                if sum(row[x + i] for row in grid[y:y+3]) != target:
                    return False

            diag1 = grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2] != target
            diag2 = grid[y+2][x] + grid[y + 1][x + 1] + grid[y][x + 2] != target
            if  diag1 or diag2 or seen != {1,2,3,4,5,6,7,8,9}:
                return  False
            
            return True
            

        rows = len(grid)
        cols = len(grid[0])
        
        if rows < 3 or cols < 3:
            return 0

        count = 0
        for y in range(rows-2):
            for x in range(cols-2): 
                if checkSquare(x,y):
                    count += 1 
        return count
