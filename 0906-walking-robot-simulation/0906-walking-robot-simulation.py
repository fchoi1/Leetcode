class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [(0,1), (1,0), (0,-1), (-1, 0)]
        dIdx, x, y = 0, 0, 0
        oSet = {(x,y) for x,y in obstacles}
        maxDist = 0
        for c in commands:
            if c == -1:
                dIdx = (dIdx + 1) % 4
            elif c == -2:
                dIdx = (dIdx - 1) % 4
            else:
                dx, dy = direction[dIdx]

                for _ in range(c):
                    x += dx 
                    y += dy
                    if (x,y) in oSet:
                        x -= dx
                        y -= dy
                        break
            maxDist = max( x * x + y * y, maxDist )
            print(x, y)
        return maxDist