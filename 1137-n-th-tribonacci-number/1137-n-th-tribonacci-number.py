class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        for _ in range(n):
            a,b,c = b,c,a + b + c
        return a
    
        
