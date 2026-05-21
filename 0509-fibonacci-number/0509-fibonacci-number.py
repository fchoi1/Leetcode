class Solution:
    def fib(self, n: int) -> int:

        prev = 0
        curr = 1

        if n == 0:
            return 0
        if n == 1:
            return 1

        for _ in range(n - 1):
            temp = curr
            curr += prev
            prev = temp
        
        return curr
        