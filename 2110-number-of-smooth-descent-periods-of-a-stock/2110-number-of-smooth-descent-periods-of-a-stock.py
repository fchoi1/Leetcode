class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        periods = 1
        smooth = 1
        for prev, curr in zip(prices, prices[1:]):
            if prev - curr == 1:
                smooth += 1
            else:
                smooth = 1
            periods += smooth

        return periods
