class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # greedy, dp

        ans = 0
        N = len(nums)
        dp = [-1 for _ in range(N)]
        dp[0] = 0

        for i in range(N):
            n1 = nums[i]
            for j in range(i + 1, N):
                n2 = nums[j]
                if abs(n1 - n2) <= target and dp[i] >= 0:
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[-1] 