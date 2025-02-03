class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = desc = inc = 1
        for a,b in zip(nums, nums[1:]):
            if b > a:
                inc += 1
                desc = 1
            elif a > b:
                inc = 1
                desc += 1
            else:
                inc = desc = 1
            longest = max(longest, inc, desc)
        return longest
        