class Solution:
    def maxDifference(self, s: str) -> int:

        min_a2 = inf
        max_a1 = -inf

        counts = Counter(s)
        diff = -inf

        for c in counts.values():
            if c % 2 == 0:
                min_a2 = min(min_a2, c)
            else:
                max_a1 = max(max_a1, c)
                
            diff = max(diff, max_a1 - min_a2)
                
        return diff


        