class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = defaultdict(int)
        total = 0
        for a,b in dominoes:
            counts[(min(a,b), max(a,b))] += 1
            total += counts[(min(a,b), max(a,b))] - 1
            
        return total
        