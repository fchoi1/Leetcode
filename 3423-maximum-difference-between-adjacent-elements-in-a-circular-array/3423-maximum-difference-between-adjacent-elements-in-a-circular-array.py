class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        dist = abs(nums[0] - nums[-1])

        for a,b in zip(nums, nums[1:]):
            dist = max(dist, abs(a-b))
        return dist
        