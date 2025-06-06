class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        overlaps = 0
        currEnd = float('-inf')
        for start, end  in intervals:
            if start < currEnd:
                currEnd = min(end, currEnd)
                overlaps += 1
            else:
                currEnd = end
        return overlaps  
                