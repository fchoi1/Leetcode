class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0
        i = 32
        while n:
            i -= 1
            if n & 1:
                val += 2 ** i
            n >>= 1
        return val
        