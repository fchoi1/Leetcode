class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        # we care about 1 zero'
        maxLen = 0
        slow = 0
        zeros = 0
        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1

            while zeros > 1:
                if nums[slow] == 0:
                    zeros -= 1
                slow += 1
            maxLen = max(maxLen, i - slow)
          
        return maxLen
        