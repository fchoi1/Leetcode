class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        
        N = len(strategy)

        maxProfit = profitTemp = 0
        for i, (p,s) in enumerate(zip(prices, strategy)):
            maxProfit += p * s
            if i < k:
                profitTemp += p * s

        profit = sum(prices[k//2:k])
        currProfit = maxProfit - profitTemp + profit
        maxProfit = max(maxProfit, currProfit)

        # sliding window
        for i in range(k, N):
            
            # add previous profit
            currProfit += prices[i-k] * strategy[i-k]

            # nullify curr
            currProfit -= prices[i] * strategy[i]

            # sell curr
            currProfit += prices[i]

            # hold mid
            mid = i - k//2
            currProfit -= prices[mid]


            # print(currProfit, "prev",  prices[i-k] , strategy[i-k], "miod", mid,  prices[mid], "curr", i, prices[i] )

            maxProfit = max(maxProfit, currProfit)

            

        
        return maxProfit