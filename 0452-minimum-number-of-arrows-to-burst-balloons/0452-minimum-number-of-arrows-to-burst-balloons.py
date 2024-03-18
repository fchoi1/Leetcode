class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        c = 1
        currEnd = points[0][1]
        for start, end in points:
            if start > currEnd:
                c += 1
                currEnd = end
            else:
                currEnd = min(currEnd,end)
        return c
