
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = defaultdict(set)
        maxCount = 1
        currSlope = None
        for i, (x1, y1) in enumerate(points[:-1]):
            for x2, y2 in points[i+1:]:
                if y1 == y2:
                    m = 0
                    b = y1
                elif x1 == x2: 
                    m = float('inf')
                    b = x1
                else:
                    m = (y1 - y2) / (x1-x2)
                    b = y1 - m * x1
                s = (m,b)
                slopes[s].add((x1,y1))
                slopes[s].add((x2,y2))
                if len(slopes[s]) > maxCount:
                    maxCount = len(slopes[s]) 
                    currSlope = s
        return maxCount 


        