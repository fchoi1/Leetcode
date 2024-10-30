class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        def getLIS(nums: List[int]):
            dp = []
            for i, n in enumerate(nums):
                total = 1
                for j, n2 in enumerate(nums[:i]):
                    if n > n2:
                        total = max(total, dp[j] + 1)
                dp.append(total)
            return dp
        
        prefix = getLIS(nums)
        prefix_end = getLIS(nums[::-1])
        min_val = 0
        for a,b in zip(prefix, prefix_end[::-1]):
            if a != 1 and b != 1:
                min_val = max(min_val, a + b)
        return len(nums) - min_val + 1