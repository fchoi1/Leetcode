class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binStr = bin(n)
        return binStr.count('1') == 1 and n > 0
        