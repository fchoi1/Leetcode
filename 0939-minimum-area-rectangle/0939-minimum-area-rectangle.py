class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xSet = defaultdict(set)
        for x,y in points:
            xSet[x].add(y)
        area = inf
        for i,p1 in enumerate(points[:-1]):
            for p2 in points[i+1:]:
                x1, y1 = p1
                x2, y2 = p2
                if x1 == x2 or y1 == y2:
                    continue
                if y2 in xSet[x1] and  y1 in xSet[x2]:
                    area = min(area, abs(x2-x1) * abs(y2-y1))
        return area if area != inf else 0