class Solution:
    def countOdds(self, low: int, high: int) -> int:
        val = (high - low) // 2
        if high % 2 == 0 and low % 2 == 0:
            return val
        return val + 1