class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

   
        N = len(s)
        # backward dp
        # represents if you can reach the start from i
        # sldiing window

        #  0  1 1 0 1 0 1 0 0
        # 3, 5 

        dp = [False] * N
        dp[0] = True

        pre = 0

        for i in range(N):

            minIdx = i - minJump
            maxIdx = i - maxJump - 1


            if minIdx >= 0 and dp[minIdx]:
                pre += 1
            
            if maxIdx >= 0 and  dp[maxIdx]:
                pre -= 1

            
            if s[i] == '0' and pre > 0:
                dp[i] = True

        

        return dp[-1]