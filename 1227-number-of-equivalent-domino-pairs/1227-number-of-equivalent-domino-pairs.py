class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = defaultdict(int)
        for a,b in dominoes:
            counts[(min(a,b), max(a,b))] += 1
            # total += counts[(min(a,b), max(a,b))] - 1
        total = 0
        for c in counts.values():
            total += c * (c - 1) // 2
        return total
        