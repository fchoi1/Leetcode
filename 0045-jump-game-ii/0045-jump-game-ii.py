class Solution:
    def jump(self, nums: List[int]) -> int:

        # 
        # backwards
        N = len(nums)
        dp = [inf] * N 
        dp[0] = 0

        for i,n in enumerate(nums):
            for j in range(n):
                # print("index", i, j, "len", len(dp))
                if j + i + 1 >= N:
                    break
                # print("set index", i+j, dp[i+j], dp[i])
                dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)
                # print("done set index", i+j, dp[i+j])
        print(dp)
                



        return dp[-1]
