class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = {(a,b) for a,b in intervals}

        N = len(intervals)

        for i in range(N):
            a,b = intervals[i]
            for j in range(i + 1, N):
                c,d = intervals[j]
                if c <= a and b <= d:
                    ans.discard((a,b))

                if a <= c and d <= b:
                    ans.discard((c,d))

        return len(ans)
        