class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        
        dp = [(d,p) for d, p in zip(difficulty, profit)]
        dp.sort()
        worker.sort()
        profit = []

        i = maxProfit = 0
        d,p = dp[0]
        currP = 0
        
        for w in worker:
            while w >= d:
                currP = max(currP, p)
                i += 1
                if i >= len(dp):
                    break
                d,p = dp[i]
            maxProfit += currP
        return maxProfit
