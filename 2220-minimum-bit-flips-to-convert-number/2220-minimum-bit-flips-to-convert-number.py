class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')
        flips = 0
        while start or goal:
            if start & 1 != goal & 1:
                flips += 1
            start >>= 1
            goal >>= 1
        return flips
        