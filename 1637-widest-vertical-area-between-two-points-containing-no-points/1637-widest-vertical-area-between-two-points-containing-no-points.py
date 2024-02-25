class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0][0]
        diff = 0
        for x, y in points:
            if x != prev:
                diff = max(x - prev, diff)
            prev = x
        return diff
            
        