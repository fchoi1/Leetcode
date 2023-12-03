class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i,[x,y] in enumerate(points[1:]):
            dx = abs(x - points[i][0])
            dy = abs(y - points[i][1])
            h = min(dx, dy)
            time += h + abs(dx-dy)
            currX, currY = x,y
        return time
            
            
            
        