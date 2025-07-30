class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 1
        curr = 0
        largest = max(nums)
        for n in nums:
            if n == largest:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 0
        return max(longest, curr)