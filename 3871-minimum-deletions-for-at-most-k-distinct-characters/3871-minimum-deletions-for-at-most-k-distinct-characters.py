class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = Counter(s)

        sorted_c = sorted(counts.values())
        N = len(sorted_c)
        if N <= k:
            return 0
        return sum(sorted_c[:N-k])

        