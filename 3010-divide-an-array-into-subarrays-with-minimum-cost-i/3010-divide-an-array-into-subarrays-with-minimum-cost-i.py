class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # heap
        # sort

        return nums[0] + sum(sorted(nums[1:])[:2])