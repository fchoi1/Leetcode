class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]
        
        minStart = newInterval[0]
        maxEnd = newInterval[1]
        if minStart > intervals[-1][1]:
            return intervals + [newInterval] 
        if maxEnd < intervals[0][0]:
            return [newInterval] + intervals

        firstInt = None
        prev = None
        ignore = set()
        for (start, end) in intervals:
            # Overlaps
            if (end >= minStart and end <= maxEnd) or (start >= minStart and start <= maxEnd) or (newInterval[0] >= start and newInterval[1] <= end):
                if not firstInt:
                    firstInt = (start, end)
                minStart = min(minStart, start)
                maxEnd = max(maxEnd, end)
                ignore.add((start, end))
            # No Overlaps
            if prev and newInterval[0] > prev[1] and newInterval[1] < start and not firstInt:
                firstInt = (start, end)
                break
            if start > maxEnd:
                break
            prev = (start, end)
        res = []
        for (start, end) in intervals:
            if (start, end) == firstInt:
                res.append((minStart, maxEnd))

            if (start, end) in ignore:
                continue
            
            res.append((start, end))
        return res        