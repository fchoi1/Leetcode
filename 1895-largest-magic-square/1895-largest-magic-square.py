class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        

        def isMagic(x,y,length):
            target = sum(grid[y][dx] for dx in range(x, x + length))
            
            # diag
            diag1 = sum(grid[y + i][x + i] for i in range(length))
            diag2 = sum(grid[y + length - i - 1][x + i] for i in range(length))
            if diag1 != target:
                return False
            if diag2 != target:
                return False
            
            for i in range(length):
                # rows
                row = sum(grid[y + i][dx] for dx in range(x, x + length))
                if row != target:
                    return False

                # cols
                col = sum(grid[dy][x + i] for dy in range(y, y + length))
                if col != target:
                    return False
            return True

        W = len(grid[0])
        H = len(grid)

        maxK = 1
        

        for n in range(1, min(W, H) + 1):
            found = False
            for y in range(H - n + 1):
                for x in range(W - n + 1):
                    if isMagic(x, y, n):
                        maxK = n
                        found = True
                        break
                if found:
                    break
   
        return maxK