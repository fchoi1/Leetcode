class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        for i,c in enumerate(str(n)):
            sign = 1 if i % 2 == 0 else -1
            result += sign * int(c)
        return result
        