class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binStr = bin(n)[2:]
        for prev,curr in zip(binStr, binStr[1:]):
            if prev == curr:
                return False
        return True