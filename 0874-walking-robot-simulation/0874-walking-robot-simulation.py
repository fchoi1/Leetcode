class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob_map = set()

        for x, y in obstacles:
            ob_map.add((x,y))

        x = y = 0
        d = 0 # 0 North, 1 East, 2 South, 3 West
        dev = [[0,1],[1,0],[0,-1],[-1,0]]
        farthest = 0

        for n in commands:
            if n == -1:
                d = (d + 1) % 4
            elif n == -2:
                d = (d - 1) % 4
            else:
                dx, dy = dev[d]
                for _ in range(n):
                    if (x + dx, y + dy) in ob_map:
                        break
                    x += dx
                    y += dy
                farthest = max(farthest, x**2 + y ** 2)
        
        return farthest
                


        