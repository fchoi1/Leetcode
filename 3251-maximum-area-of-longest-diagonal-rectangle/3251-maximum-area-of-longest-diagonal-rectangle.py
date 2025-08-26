class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max((sqrt(a**2 + b**2), a * b) for a,b in dimensions)[1]