class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        running = 0
        minLen = inf
        for i, val in enumerate(nums):
            running += val
            while running >= target:
                minLen = min(minLen, i - left + 1)
                running -= nums[left]
                left += 1
            
        return 0 if minLen == inf else minLen
        