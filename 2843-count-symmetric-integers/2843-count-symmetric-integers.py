class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        total = 0
        for i in range(low, high + 1):
            N = len(str(i))
            if N % 2 == 1:
                continue
            left = sum(int(n) for n in str(i)[:N//2])
            right = sum(int(n) for n in str(i)[N//2:])
            
            if left == right:
                total += 1
        return total