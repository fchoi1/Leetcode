class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        return sum(b == '1' for b in bin(n)[2:]) == 1
        