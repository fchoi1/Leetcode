class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i, n in enumerate(nums):
            total = 1
            for j, n2 in enumerate(nums[:i]):
                if n > n2:
                    total = max(total, dp[j] + 1)
            dp.append(total)
        return max(dp)