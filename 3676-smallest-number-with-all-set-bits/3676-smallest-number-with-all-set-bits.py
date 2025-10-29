class Solution:
    def smallestNumber(self, n: int) -> int:
        curr = 0
        for _ in range(10):
            curr <<= 1
            curr |= 1
            if curr >= n:
                return curr
        return curr