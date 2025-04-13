class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # backtrack groud up
        four = n // 2
        five = n - four
        mod = 10 ** 9 + 7
        return (pow(4, four, mod) * pow(5, five, mod)) % mod