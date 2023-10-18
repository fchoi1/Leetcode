class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key= lambda x: (x[0], x[1]))
        newIntervals = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > newIntervals[-1][1]:
                newIntervals.append(interval)
            else:
                newIntervals[-1] = [min(newIntervals[-1][0],interval[0]), max(newIntervals[-1][1],interval[1])]

        return newIntervals
        