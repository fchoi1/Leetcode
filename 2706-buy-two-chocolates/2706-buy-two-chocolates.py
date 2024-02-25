class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min(prices[0], prices[1])
        min2 = max(prices[0], prices[1])
        for p in prices[2:]:
            if p < min1:
                min2 = min1
                min1 = p
            elif p < min2:
                min2 = p
        return money - min1 - min2 if (min1 + min2) <= money else money


        