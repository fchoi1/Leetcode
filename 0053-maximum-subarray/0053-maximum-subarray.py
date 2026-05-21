class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-inf] * len(nums)
        for i,n in enumerate(nums):
            if i == 0:
                dp[i] = n
            else:
                dp[i] = max(n, dp[i-1] + n)
        return max(dp)