class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for a,b in zip(nums, nums[1:]):
            if (a + b) % 2 == 0:
                return False
        return True