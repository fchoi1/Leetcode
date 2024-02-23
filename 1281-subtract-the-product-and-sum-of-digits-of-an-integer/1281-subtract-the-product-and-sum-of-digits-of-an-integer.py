class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        for char in str(n):
            p *= int(char)
            s += int(char)
        return p - s
        