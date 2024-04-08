class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxLength = 1
        up = down = 1
        prev = nums[0]
        for i, n in enumerate(nums[1:]):
            if n > prev:
                up += 1
                down = 1
            elif n < prev:
                up = 1
                down += 1
            else:
                up = 1
                down = 1
            prev = n
            maxLength = max(maxLength, up, down)
        return maxLength