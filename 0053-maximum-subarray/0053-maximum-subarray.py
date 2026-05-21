class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-inf] * len(nums)
        ans = nums[0]
        for i,n in enumerate(nums):
            if i == 0:
                dp[i] = n
            else:
                dp[i] = max(n, dp[i-1] + n)
            ans = max(ans, dp[i])
        return ans
