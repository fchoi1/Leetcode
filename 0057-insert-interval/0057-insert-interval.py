class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        newStart = newInterval[0]
        newEnd = newInterval[1]
        for start, end in intervals:
            if end < newInterval[0] or start > newInterval[1]:
                if start > newInterval[1] and newStart is not None:
                    res.append([newStart, newEnd])
                    newStart = None
                res.append([start,end])
                continue
            newStart = min(newStart, start)
            newEnd = max(newEnd, end)
        print(res)
        if newStart is not None:
            res.append([newStart, newEnd])
        return res
        