class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = sum(int(c) for c in str(n))
        for char in str(n):
            p *= int(char)
        return p - s
        