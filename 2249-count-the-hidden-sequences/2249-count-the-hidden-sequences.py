class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        maxVal = 0
        minVal = 0
        curr = 0
        for d in differences:
            curr += d
            maxVal = max(maxVal, curr)
            minVal = min(minVal, curr)

        r = maxVal - minVal
        if r > (upper - lower):
            return 0
        return (upper - lower) - r + 1

