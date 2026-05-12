class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # min, gained
        # sort by min energy required, then gained

        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        curr = extra = 0
        for actual, need in tasks:
            gain = need - actual

            if curr < need:
                extra += need - curr
                curr = 0
            else:
                curr -= need
            curr += gain
        
        return extra

