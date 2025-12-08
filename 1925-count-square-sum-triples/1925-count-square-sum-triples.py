class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1,n):
            for b in range(1,n):
                c = sqrt(a**2 + b**2) 
                if c == int(c) and c <= n:
                    ans += 1
        return ans
