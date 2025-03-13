class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2:
            return True

        for prev, curr in zip(nums, nums[1:]):
            if prev + curr >= m:
                return True
        return False
        