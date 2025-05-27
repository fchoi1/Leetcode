class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n+1)//2
        n_div = n // m
        n_div_total = n_div * (n_div+1) * m // 2

     
        return total_sum - 2 * n_div_total
        
        