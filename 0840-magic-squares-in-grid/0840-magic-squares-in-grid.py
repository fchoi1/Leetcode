class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        

        def isMagic(startX, startY): # top left
            numSet = set()
            # diags
            diag1 = grid[startY][startX] + grid[startY + 1][startX + 1] + grid[startY + 2][startX + 2] 
            diag2 = grid[startY][startX + 2] + grid[startY + 1][startX + 1] + grid[startY + 2][startX] 
            print("diag", startX, startY, diag1, diag2)
            if diag1 != 15 or diag2 != 15:
                return False

            # row / col
            for x in range(3):
                if sum(row[startX + x] for row in grid[startY: startY + 3]) != 15:
                    return False

                for y in range(3):
                    if sum(grid[y + startY][startX: startX + 3]) != 15:
                        return False
                    numSet.add(grid[y + startY][x + startX])
                    
            print(numSet, "cstart", startX, startY)
            return numSet == {1,2,3,4,5,6,7,8,9}
        

        H = len(grid)
        W = len(grid[0])
        ans = 0
        for y in range(0, H - 2):
            for x in range(0, W - 2):
                if isMagic(x,y):
                    ans += 1
        return ans