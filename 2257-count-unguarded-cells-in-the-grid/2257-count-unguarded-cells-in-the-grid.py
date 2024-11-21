class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        cells = [[1] * n for _ in range(m)]
                
        wallSet = set()
        guardSet = set()

        for x,y in walls:
            wallSet.add((y,x))
        for x,y in guards:
            guardSet.add((y,x))

        for y in range(m):
            g = False
            for x in range(n):
                if (x,y) in wallSet:
                    g = False
                    cells[y][x] = 0
                elif (x,y) in guardSet:
                    g = True
                    cells[y][x] = 0
                else:
                    if g:
                        cells[y][x] = 0
            g = False
            for x in range(n-1,-1,-1):
                if (x,y) in wallSet:
                    g = False
                    cells[y][x] = 0
                elif (x,y) in guardSet:
                    g = True
                    cells[y][x] = 0
                else:
                    if g:
                        cells[y][x] = 0

        for x in range(n):
            g = False
            for y in range(m):
                if (x,y) in wallSet:
                    g = False
                    cells[y][x] = 0
                elif (x,y) in guardSet:
                    g = True
                    cells[y][x] = 0
                else:
                    if g:
                        cells[y][x] = 0
            g = False       
            for y in range(m-1,-1,-1):
                if (x,y) in wallSet:
                    g = False
                    cells[y][x] = 0
                elif (x,y) in guardSet:
                    g = True
                    cells[y][x] = 0
                else:
                    if g:
                        cells[y][x] = 0
       
        return sum(sum(r) for r in cells)
