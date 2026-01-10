class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices.copy()
        stack = []

        for i,p in enumerate(prices):
            if stack:
                while stack and p <= stack[-1][1]:
                    idx, price = stack.pop()
                    ans[idx] = price - p
            stack.append((i,p))
        return ans


           
        