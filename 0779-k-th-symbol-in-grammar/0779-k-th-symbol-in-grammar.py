class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        path = []
        k -= 1
        for _ in range(n):
            path.append(k)
            k //= 2 
        
        prev = 0
        for val in path[::-1]:
            if (prev == 0 and val % 2 == 0) or (prev and val % 2 == 1):
                prev = 0
            else:
                prev = 1
       
        return prev
        #        0
        #       01
        #.     01 10
        #    01 10 10 01
        # 01 10 10 01 10 01 01 10
        return 1
        