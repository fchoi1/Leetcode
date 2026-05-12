class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # min, gained

        # sort by min energy required, then gained

        h = []
        for actual, need in tasks:
            gain = need - actual
            heappush(h, (-gain, need))

        minEnergy = -h[0][0]
        curr = minEnergy
        extra = 0
        while h:
            gain, need = heappop(h)
            gain = -gain

            if curr < need:
                extra += need - curr
                curr = 0
            else:
                curr -= need
            curr += gain
        
        return minEnergy + extra

