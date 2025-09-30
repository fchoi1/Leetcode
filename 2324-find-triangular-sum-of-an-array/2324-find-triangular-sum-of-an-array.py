class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums) != 1:
            nums = [ (prev + curr) % 10 for prev, curr in zip(nums, nums[1:]) ]
        return nums[0]