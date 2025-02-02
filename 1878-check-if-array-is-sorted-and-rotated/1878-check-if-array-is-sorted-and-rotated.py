class Solution:
    def check(self, nums: List[int]) -> bool:
        desc = 0
        for a,b in zip(nums, nums[1:]):
            if b < a:
                desc += 1
                if desc > 1:
                    return False
        return nums[-1] <= nums[0] if desc == 1 else True