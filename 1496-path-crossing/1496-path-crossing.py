class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set()
        dirMap = {"N": (0,1), "S":(0,-1), "E": (1,0), "W":(-1,0)}
        for char in path:
            visited.add((x,y))
            dx, dy = dirMap[char]
            x += dx
            y += dy
            if (x,y) in visited:
                return True
        return False
        