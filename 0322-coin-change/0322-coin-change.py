class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        largest = max(coins)
        dpCheck = []
        for n in range(amount+1):
            minCoin = float('inf')
            for coin in coins:
                if coin == n:
                    minCoin = 1
                elif coin < n:
                    minCoin = min(minCoin, dpCheck[n-coin] + 1)
            dpCheck.append(minCoin)
        return dpCheck[-1] if  dpCheck[-1] != float("inf") else -1
        