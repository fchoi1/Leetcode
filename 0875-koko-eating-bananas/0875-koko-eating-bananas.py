class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcHours(k):
            return sum(math.ceil(p/k) for p in piles)
        
        maxK = max(piles)
        minK = math.ceil(sum(piles) /  h)
        
        while maxK > minK:
            half = (maxK + minK) // 2
            if calcHours(half) <= h:
                maxK = half
            else:
                minK = half+1
        return maxK
        
            