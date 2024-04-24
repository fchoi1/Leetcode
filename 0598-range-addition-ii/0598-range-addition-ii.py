class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minX = n
        minY = m
        for a,b in ops:
            minY = min(minY, a)
            minX = min(minX, b)
        return minX * minY
            
