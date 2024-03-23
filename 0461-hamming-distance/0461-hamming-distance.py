class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val = x ^ y
        return val.bit_count()