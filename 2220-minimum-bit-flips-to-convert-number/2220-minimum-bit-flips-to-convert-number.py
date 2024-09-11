class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0

        while start or goal:
            s = start & 1 if start else 0
            g = goal & 1 if goal else 0
            start >>= 1
            goal >>= 1
            if s != g:
                flips += 1
        return flips
        