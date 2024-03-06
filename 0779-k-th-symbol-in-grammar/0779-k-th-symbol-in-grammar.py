class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        path = []
        k -= 1
        for _ in range(n):
            path.append(k)
            k //= 2 
        
        prev = 0
        for val in path[::-1]:
            prev = (prev and val % 2 == 0) or (not prev and val % 2 == 1)
        return int(prev)
   
        