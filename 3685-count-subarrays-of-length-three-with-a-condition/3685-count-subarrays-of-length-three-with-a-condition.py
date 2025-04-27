class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for a,b,c in zip(nums, nums[1:], nums[2:]):
            if a + c == b / 2:
                count += 1
        return count