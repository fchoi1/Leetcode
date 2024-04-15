class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        
        def getMaxDist(skip):  
            maxVal = 0
            maxPoints = (0,1)
            for a,b in [[1,1],[-1,1],[1,-1],[-1,-1]]:
                start = points[1] if skip == 0 else points[0]
                smallIndex = 1 if skip == 0 else 0
                smallest = a * start[0] + b * start[1] 
                
                for i,(x,y) in enumerate(points):
                    if i == skip:
                        continue
                    curr = a * x + b * y
                    if curr-smallest > maxVal:
                        maxPoints = (i, smallIndex)
                        maxVal = curr-smallest
                    if curr < smallest:
                        smallIndex = i
                        smallest = curr
            return maxVal, maxPoints

        maxDist = float('inf')
        N = len(points)
        _, maxPoints = getMaxDist(N)
        print(maxPoints)
        dist1 = getMaxDist(maxPoints[0])
        dist2 = getMaxDist(maxPoints[1])
        print(dist1, dist2)
        return min(dist1[0], dist2[0])
        