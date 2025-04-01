class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp backtrack?


        currMax = 0

        # backwards
        N = len(questions)
        dp = [0 for _ in range(N)]
        for i in range(N-1, -1, -1):
            
            point, brain =  questions[i]
            # print("index", i, "p,b", point, brain, dp, "index", i + brain)

            if brain + i + 1 >= N:
                dp[i] = max(currMax, point)
            else:
                dp[i] = max(currMax, point + dp[brain + i + 1])
            currMax =  max(currMax, dp[i])

        # print(dp)
        # 58 + 65 = 123
        return currMax