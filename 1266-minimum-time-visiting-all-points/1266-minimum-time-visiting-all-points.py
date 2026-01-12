class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        for prev, curr in zip(points, points[1:]):
            px, py = prev
            cx, cy = curr

            maxDiff = max(abs(px - cx), abs(py - cy))
            minDiff = min(abs(px - cx), abs(py - cy))
            diff = maxDiff - minDiff

            time += diff + minDiff

        return time