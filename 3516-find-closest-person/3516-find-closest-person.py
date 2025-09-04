class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff = abs(x-z)
        diff2 = abs(y-z)

        if diff == diff2:
            return 0

        return 1 if diff < diff2 else 2