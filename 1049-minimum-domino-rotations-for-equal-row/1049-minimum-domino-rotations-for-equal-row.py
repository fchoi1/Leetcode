class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t_counts = Counter(tops)
        b_counts = Counter(bottoms)
        N = len(tops)

        flips = inf
        if all(tops[0] in [a,b] for a,b in zip(tops, bottoms)):
            flips = min(flips, N - t_counts[tops[0]], N - b_counts[tops[0]])
            
        if all(bottoms[0] in [a,b] for a,b in zip(tops, bottoms)):
            flips = min(flips, N - t_counts[bottoms[0]], N - b_counts[bottoms[0]])

        return flips if flips != inf else -1