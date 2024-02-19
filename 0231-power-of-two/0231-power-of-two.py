class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return int(log(n,2)) == round(log(n,2), 10)