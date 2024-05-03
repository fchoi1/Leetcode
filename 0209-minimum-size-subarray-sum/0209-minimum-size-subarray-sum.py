class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = currSum = 0
        minLen = inf
        for i, val in enumerate(nums):
            currSum += val
            while currSum >= target:
                minLen = min(minLen, i-slow)
                currSum -= nums[slow]
                slow += 1
        
        return 0 if minLen == inf else minLen + 1