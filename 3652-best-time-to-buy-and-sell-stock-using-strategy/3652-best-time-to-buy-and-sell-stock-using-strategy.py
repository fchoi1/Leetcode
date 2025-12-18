class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # sliding window
        profit = 0
        for p, s in zip(prices, strategy):
            profit += s * p

        # idx = 0
        idx = 0
        # hold
        currProfit = profit
        maxProfit = profit
        # print('curr', profit)
        while idx < k // 2:
            p,s = prices[idx], strategy[idx]

            currProfit -= p * s
            idx += 1

        # sell
        while idx < k:
            p,s = prices[idx], strategy[idx]

            if s == 0:
                currProfit += p
            elif s == -1:
                currProfit += 2 * p
            idx += 1

        # print("forst", currProfit)
        maxProfit = max(maxProfit, currProfit)

        for i in range(k, len(prices)):
            prevP, prevS = prices[i - k], strategy[i - k]
            halfP, halfS = prices[i - k//2], strategy[i - k//2]
            
            currProfit += prevP * prevS
            
            currProfit -= halfP 
          
            
            p,s = prices[i], strategy[i]

            if s == 0:
                currProfit += p
            elif s == -1:
                currProfit += 2 * p
                
            # print("after",  currProfit, p, s, prevP * prevS, halfP * halfS)

            maxProfit = max(maxProfit, currProfit)
            
        return maxProfit