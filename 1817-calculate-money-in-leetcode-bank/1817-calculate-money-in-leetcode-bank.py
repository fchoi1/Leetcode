class Solution:
    def totalMoney(self, n: int) -> int:
        times = n // 7
        div = n % 7
        total = 0
        for i in range(1, times + 1):
            total += 7 * (i + i + 6) // 2

        total += int(div * (times + 1 + times + div) / 2)

        return total