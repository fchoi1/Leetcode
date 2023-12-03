class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        # check on same diag y = mx + b   b=(y-x)
        # move towards diag
        time = 0
        currX, currY = points[0]
        for x,y in points:
            if currX == x and currY == y:
                continue
            dx = abs(x - currX)
            dy = abs(y - currY)
            h = min(dx, dy)
            time += h + abs(dx-dy)
            currX, currY = x,y
        return time
            
            
            
        