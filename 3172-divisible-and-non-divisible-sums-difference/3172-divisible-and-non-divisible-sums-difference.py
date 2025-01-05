class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        n1 =  sum(i for i in range(0,n+1,m))
        return total - 2 * n1