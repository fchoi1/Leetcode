class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        currMin = nums[0]
        diff = -1
        for n in nums:
            currMin = min(currMin, n)
            if n - currMin > 0:
                diff = max(diff, n - currMin)
        return diff
        