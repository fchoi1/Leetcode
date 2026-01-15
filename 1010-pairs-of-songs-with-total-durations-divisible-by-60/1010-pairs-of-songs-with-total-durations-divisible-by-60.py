from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        times = defaultdict(int)
        reduced = [t % 60 for t in time]
        c = 0
        for t in reduced:
            if t in times or t == 0:
                c += times[60] if t == 0 else times[t]
            times[(60 - t)] += 1
        return c
        