class Solution:
    def coloredCells(self, n: int) -> int:
        n -= 1
        arithmetic = 2 * n ** 2 + 2 * n
        return 1 + arithmetic