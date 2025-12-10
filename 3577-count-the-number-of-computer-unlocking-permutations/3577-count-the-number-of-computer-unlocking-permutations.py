class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        zero = complexity[0]
        mod = 10 ** 9 + 7

        for n in complexity[1:]:
            if n <= zero:
                return 0
        @cache
        def factorial(x):
            if x < 2:
                return 1
            
            return x * factorial(x - 1) % mod
        
        return factorial(len(complexity)-1) % mod
