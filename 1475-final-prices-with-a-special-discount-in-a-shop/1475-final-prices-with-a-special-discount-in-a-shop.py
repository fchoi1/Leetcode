class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices

        for i,n in enumerate(prices):
            while stack and n <= stack[-1][0]:
                curr, index = stack.pop()
                ans[index] = curr - n
            stack.append((n, i))
        return ans

           
        